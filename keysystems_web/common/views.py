from django.http import JsonResponse, HttpRequest
from django.db.models import Count, Q
from django.shortcuts import render

import json
import logging

from .models import Order, Message
from .serializers import OrderSerializer, MessageSerializer
from .logs import log_error
from enums import ChatType


def get_order_data(request: HttpRequest, order_id):
    log_error('>>>>>>>>>>>>', wt=False)
    try:
        log_error(f'{type(order_id)} {order_id}', wt=False)
        order = Order.objects.filter(id=order_id).first()
        # messages = Message.objects.filter(order=order).order_by('created_at')
        messages = Message.objects.order_by('created_at')

        client_messages = messages.filter(chat=ChatType.CLIENT.value)
        curator_messages = messages.filter(chat=ChatType.CURATOR.value)

        # client_unviewed_message = client_messages.filter(~Q(view_message__user_ks=request.user)).distinct().count()
        # curator_unviewed_message = curator_messages.filter(~Q(view_message__user_ks=request.user)).distinct().count()
        return JsonResponse(
            {
                'order': OrderSerializer(order).data,
                'client_chat': MessageSerializer(client_messages.all(), many=True).data,
                'curator_chat': MessageSerializer(curator_messages.all(), many=True).data,
                'chat': MessageSerializer(messages.all(), many=True).data,
                'user_id': 4,
                # 'unv_msg_client': client_unviewed_message,
                # 'unv_msg_curator': curator_unviewed_message
                'unv_msg_client': 3,
                'unv_msg_curator': 4
            },
            safe=False
        )
    except Exception as ex:
        log_error(ex)
        return JsonResponse({'error': 'not found'}, status=404)


def index(request: HttpRequest):
    return render(request, "chat/index.html")


def room(request: HttpRequest, room_name: str = None):
    log_error(f'room_name: {room_name}\n', wt=False)
    messages = Message.objects.order_by('created_at')

    client_messages = messages.filter(chat=ChatType.CLIENT.value)
    curator_messages = messages.filter(chat=ChatType.CURATOR.value)

    if not room_name:
        room_name = 'test'

    context = {
        "room_name": room_name,
        'client_chat': json.dumps(MessageSerializer(client_messages.all(), many=True).data),
        'curator_chat': json.dumps(MessageSerializer(curator_messages.all(), many=True).data),
        'chat': json.dumps(MessageSerializer(messages.all(), many=True).data),
        'user_id': 4
    }
    return render(request, "chat/room.html", context)


# def chat_view(request, room_name):
#     return render(request, f'chat/{room_name}.html', {
#         'room_name': room_name,
#         's_data': random.randint(1000, 9999)
#     })


