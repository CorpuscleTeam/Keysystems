from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

import json
import random

from . import utils as ut
from .logs import log_error
from .models import Message, UserKS, Order, OrderCurator, Notice
from .serializers import MessageSerializer, UserKSSerializer
from enums import ChatType, NoticeType, MsgType, notices_dict, EditOrderAction


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        log_error(wt=False, message=f'connect\n'
                                    f'{self.scope["url_route"]}\n'
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
    def receive(self, text_data):
        data_json: dict = json.loads(text_data)
        log_error(wt=False, message=f'receive\n{data_json}\n')

        if data_json['event'] == EditOrderAction.MSG:
            user = UserKS.objects.filter(id=data_json['user_id']).first()
            log_error(wt=False, message=f'user: {user}\n')
            if user:
                order = Order.objects.select_related('from_user').filter(id=int(data_json['order_id'])).first()
                curators = OrderCurator.objects.select_related('user').filter(order=order).all()

                # сохраняем сообщение
                new_message = Message(
                    type_msg=MsgType.MSG.value,
                    from_user=user,
                    # chat=ChatType.CLIENT.value if data_json['chat'] == '#tab2' else ChatType.CURATOR.value,
                    chat=data_json['chat'],
                    order_id=int(data_json['order_id']),
                    text=data_json['message']
                )
                new_message.save()

                # рассылаем уведомления
                notice_list = [curator.user.id for curator in curators] + [order.from_user.id]
                if data_json['user_id'] in notice_list:
                    notice_list.remove(data_json['user_id'])

                notice: str = notices_dict.get(NoticeType.NEW_MSG.value)
                notice_text = notice.format(pk=order.id)

                for user_id in notice_list:
                    new_notice = Notice(
                        order=order,
                        user_ks_id=user_id,
                        type_notice=notice_text
                    )
                    new_notice.save()

                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name, {
                        "type": "chat.message",
                        'data': MessageSerializer(new_message).data,
                    }
                )

            else:
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name, {"type": "chat.message", **data_json}
                )

        # обновление списка кураторов заказа
        elif data_json['event'] == EditOrderAction.EDIT_CURATOR:
            order_id = int(data_json.get('order_id', 0))

            # если есть кого добавить
            if data_json.get('add'):
                add_user_id = int(data_json.get('add'))
                OrderCurator.objects.create(order_id=order_id, user_id=add_user_id)

            # если есть кого удалить
            if data_json.get('del'):
                del_user_id = int(data_json.get('del'))
                OrderCurator.objects.create(order_id=order_id, user_id=del_user_id)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name, {"type": "curator.list", 'order_id': order_id}
            )

        # изменить статус заказа
        elif data_json['event'] == EditOrderAction.EDIT_STATUS:
            order_id = int(data_json['order_id'])
            order = Order.objects.filter(id=order_id)
            order.status = data_json['status']
            order.save()

    # обновляет сообщения в чате
    def chat_message(self, event):
        # {'type': 'chat.message', 'message': 'рррр', 'tab': '#tab2', 'order_id': '18'}

        log_error(wt=False, message=f'chat_message\n{event}\n')

        if event.get('tab'):
            now = datetime.now()
            chat = random.choice([ChatType.CLIENT.value, ChatType.CURATOR.value])
            message = {
                'type': EditOrderAction.MSG.value,
                'from_user': {'id': 2, 'full_name': 'Тест'},
                'text': event["message"],
                'time': ut.get_time_string(now),
                'chat': chat
            }
            self.send(text_data=json.dumps({"message": message}))

        else:
            self.send(text_data=json.dumps({"message": event['data']}))

    # отправляет новый список кураторов
    def curator_list(self, event):
        log_error(wt=False, message=f'curator_list\n{event}\n')

        curators = OrderCurator.objects.filter(order_id=event['order_id']).all()
        log_error(wt=False, message=f'curators\n{curators}\n')

        context = {
            'type': EditOrderAction.EDIT_CURATOR.value,
            'curators': UserKSSerializer([curator.user for curator in curators], many=True).data,
        }

        self.send(text_data=json.dumps(context))



