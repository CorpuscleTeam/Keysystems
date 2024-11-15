import json

from keysystems_web.settings import REDIS_DB, REDIS_TTL


# сохраняем данные
async def add_online_user(room_name: str, user_id: int) -> None:
    data = []
    REDIS_DB.setex(room_name, REDIS_TTL, json.dumps(data))


# возвращаем данные
async def get_user_data(chat_id) -> dict:
    key = f"{chat_id}"
    data = REDIS_DB.get(key)
    return json.loads(data) if data else {}


# добавляет данные
# async def update_user_data(chat_id: int, key: str, value: str) -> None:
#     data = get_user_data(chat_id)
#     data[key] = value
#     save_user_data(chat_id, data)


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
from .serializers import MessageSerializer, UserKSSerializer
from enums import ChatType, NoticeType, MsgType, notices_dict, EditOrderAction, TAB, CountSelector


# окошко заявки
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        log_error(wt=False, message=f'connect\n'
                                    f'{self.scope["url_route"]}\n'
                                    f'{self.scope["user"]}\n'
                                    f'self.channel_name: {self.channel_name}')

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

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        data_json: dict = json.loads(text_data) if text_data else {'event': 'file_', 'text_data': str(text_data)}

        if data_json['event'] == EditOrderAction.MSG or data_json['event'] == EditOrderAction.FILE:
            # рассылаем уведомления
            notice_list = [curator.user.id for curator in curators] + [order.from_user.id]

            notice: str = notices_dict.get(NoticeType.NEW_MSG.value)
            notice_text = notice.format(pk=order.id)

            for user_id in notice_list:
                ...

                # обновляем циферки
                async_to_sync(self.channel_layer.group_send)(
                    f'user{user_id}',  # Имя группы
                    {
                        'type': 'update.counter',  # Это соответствует методу 'counter' в UserConsumer
                        'user_id': data_json['user_id'],
                        'selector': CountSelector.PUSH.value
                    }
                )

            # отправляем сообщение
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {
                    "type": "chat.message",
                    'data': MessageSerializer(new_message).data,
                }
            )


# оживление страницы
class UserConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    # обновляет счётчик сообщений
    def update_counter(self, event: dict):
        room_name = event['room_name']
        selector = event['selector']

        log_error(f'FFFFFFFFFFF: {event}', wt=False)
        self.send(text_data=json.dumps(event))

