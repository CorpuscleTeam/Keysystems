from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

import json
import random

from . import utils as ut
from .logs import log_error
from enums import ChatType


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        log_error(wt=False, message=f'connect\n\n'
                                    f'{self.scope["url_route"]["kwargs"]["room_name"]}\n'
                                    f'{self.scope["url_route"]["kwargs"]}\n'
                                    f'{self.scope["url_route"]}\n')

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
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        log_error(wt=False, message=f'receive\n\n'
                                    f'{text_data_json["message"]}\n'
                                    f'{text_data_json}\n'
                                    f'')

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        # message = event["message"]
        # fields = ['created_at', 'from_user', 'text', 'time']

        now = datetime.now()
        chat = random.choice([ChatType.CLIENT.value, ChatType.CURATOR.value])
        message = {
            'from_user': {'id': 2, 'full_name': 'Тест'},
            'text': event["message"],
            'time': ut.get_time_string(now),
            'chat': chat
        }
        log_error(wt=False, message=f'chat_message\n\n'
                                    f'{event["message"]}\n'
                                    f'{event}\n'
                                    f'')

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))