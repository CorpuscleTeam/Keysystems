from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

import json
import random
import os
import base64
import logging

from . import utils as ut
from . import redis_utils as ru
from .logs import log_error
from .models import Message, UserKS, Order, OrderCurator, Notice, ViewMessage
from . import consumers_utils as ut
from .serializers import SimpleOrderSerializer, UserKSSerializer
from enums import ChatType, NoticeType, MsgType, notices_dict, EditOrderAction, TAB, CountSelector


online_group_name = 'user_status_tracker'


# окошко заявки
class ChatConsumer(WebsocketConsumer):
    online_users = {}
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"group_{self.room_name}"

        # user_id = self.scope["user"].id
        #
        log_error(wt=False, message=f'connect\n'
                                    f'room_name: {self.room_name}')

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        async_to_sync(self.channel_layer.group_add)(
            "user_status_tracker",  # Имя группы для отслеживания статусов пользователей
            self.channel_name  # Канал текущего соединения
        )

        # Добавляем в онлайн
        async_to_sync(self.channel_layer.send)(
            'user_status_tracker',  # Группа для отслеживания статусов пользователей
            {
                'type': 'user_online',
                'user_id': self.scope["user"].id,
                'group': self.room_name
            }
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        data_json: dict = json.loads(text_data) if text_data else {'event': 'file_', 'text_data': str(text_data)}
        # log_error(wt=False, message=f'receive\n{data_json}'[:200])

        if data_json['event'] == EditOrderAction.MSG or data_json['event'] == EditOrderAction.FILE:
            ut.ws_proc_msg(data_json, self)

        # обновление списка кураторов заказа
        elif data_json['event'] == EditOrderAction.EDIT_CURATOR:
            ut.ws_proc_curator(event_data=data_json, ws_consumer=self)

        # изменить статус заказа
        elif data_json['event'] == EditOrderAction.EDIT_STATUS:
            ut.ws_proc_status(event_data=data_json, ws_consumer=self)

        # отмечает сообщения просмотренными
        elif data_json['event'] == EditOrderAction.VIEW_TAB:
            ut.ws_proc_view_msg(event_data=data_json, ws_consumer=self)

        # меняет софт
        elif data_json['event'] == EditOrderAction.EDIT_SOFT:
            ut.ws_proc_soft(event_data=data_json, ws_consumer=self)

    # обновляет сообщения в чате
    def chat_message(self, event):
        # {'type': 'chat.message', 'message': 'рррр', 'tab': '#tab2', 'order_id': '18'}

        # log_error(wt=False, message=f'chat_message\n{event}\n')

        if event.get('tab'):
            now = datetime.now()
            chat = random.choice([ChatType.CLIENT.value, ChatType.CURATOR.value])
            message = {
                'type_msg': EditOrderAction.MSG.value,
                'from_user': {'id': 2, 'full_name': 'Тест'},
                'text': event["message"],
                'time': ut.get_time_string(now),
                'chat': chat
            }
            self.send(text_data=json.dumps({'type': 'msg', "message": message}))

        else:
            self.send(text_data=json.dumps({'type': 'msg', "message": event['data']}))

    # отправляет новый список кураторов
    def curator_list(self, event):
        log_error(wt=False, message=f'curator_list\n{event}\n')

        curators = OrderCurator.objects.filter(order_id=event['order_id']).all()
        context = {
            'type': EditOrderAction.EDIT_CURATOR.value,
            'curators': UserKSSerializer([curator.user for curator in curators], many=True).data,
        }

        self.send(text_data=json.dumps(context))

    # отправляет новый список кураторов
    def select_status(self, event):
        log_error(wt=False, message=f'select_status\n{event}\n')
        context = {
            'type': EditOrderAction.EDIT_STATUS.value,
            'status': event['status'],
        }

        self.send(text_data=json.dumps(context))

    # отправляет новый список кураторов
    def edit_soft(self, event):
        log_error(wt=False, message=f'edit_soft\n{event}\n')
        context = {
            'type': EditOrderAction.EDIT_SOFT.value,
            'soft_id': event['soft_id'],
            'soft_name': event['soft_name'],
        }

        self.send(text_data=json.dumps(context))

    # def user_online(self, event):
    #     user_id = event['user_id']
    #     group = event['group']
    #
    #     log_error(f'1user_online', wt=False)
    #
    #     # Добавляем пользователя в онлайн статус
    #     if group not in self.online_users:
    #         self.online_users[group] = set()
    #     self.online_users[group].add(user_id)


# оживление страницы
class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"user{self.scope['user'].id}"

        # log_error(f'Летииим!!!!  {self.room_group_name}', wt=False)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        pass

    def receive_order(self, order_data: dict):
        ut.add_new_order(event_data=order_data, ws_consumer=self)

    # обновляет счётчик сообщений
    def update_counter(self, event: dict):
        # log_error(f'update_counter: {event}', wt=False)
        event['type'] = 'count_update'
        # self.send(text_data=json.dumps({'selector': selector}))
        self.send(text_data=json.dumps(event))

    def order_status(self, event: dict):
        # log_error(f'order_status: {event}', wt=False)
        event['type'] = 'order_status'
        # self.send(text_data=json.dumps({'selector': selector}))
        self.send(text_data=json.dumps(event))

    def order_soft(self, event: dict):
        # log_error(f'order_soft: {event}', wt=False)
        event['type'] = 'order_soft'
        # self.send(text_data=json.dumps({'selector': selector}))
        self.send(text_data=json.dumps(event))

    def order_add(self, event: dict):
        log_error(f'order_add: {event}', wt=False)
        # order = Order.objects.filter(id=int(event['order_id'])).first()

        # event['type'] = SimpleOrderSerializer(order).data
        event['type'] = 'add_new_order'

        self.send(text_data=json.dumps(event))


# данные о пользователях онлайн
# class UserStatusConsumer(WebsocketConsumer):
#     online_users = {}  # Это будет словарь для отслеживания пользователей
#
#     def user_online(self, event):
#         user_id = event['user_id']
#         group = event['group']
#
#         log_error(f'user_online', wt=False)
#
#         # Добавляем пользователя в онлайн статус
#         if group not in self.online_users:
#             self.online_users[group] = set()
#         self.online_users[group].add(user_id)
#
#     def user_offline(self, event):
#         user_id = event['user_id']
#         group = event['group']
#
#         log_error(f'user_offline', wt=False)
#
#         # Удаляем пользователя из онлайн статуса
#         if group in self.online_users:
#             self.online_users[group].discard(user_id)
#             if not self.online_users[group]:  # Если группа пуста, удаляем
#                 del self.online_users[group]
#
#     # Проверка, кто онлайн в конкретной группе
#     def is_user_online(self, group, user_id):
#         log_error(f'is_user_online', wt=False)
#
#         return group in self.online_users and user_id in self.online_users[group]
