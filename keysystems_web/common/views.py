from django.http import JsonResponse, HttpRequest
from django.db.models import Count, Q
from django.shortcuts import render

import json
import logging

from .models import Order, Message, OrderCurator, ViewMessage
from .serializers import OrderSerializer, MessageSerializer
from .logs import log_error
from enums import ChatType, RequestMethod, EditOrderAction


def get_order_data(request: HttpRequest, order_id):
    log_error('>>>>>>>>>>>>', wt=False)
    try:
        log_error(f'{order_id}', wt=False)

        order = Order.objects.filter(id=order_id).first()
        messages = Message.objects.filter(order=order).order_by('created_at')
        # messages = Message.objects.order_by('created_at')

        # разделяем чаты на клиентский и кураторский
        client_messages = messages.filter(chat=ChatType.CLIENT.value)
        curator_messages = messages.filter(chat=ChatType.CURATOR.value)

        room_name = f'order{order_id}'

        # для отладки
        if request.user.is_authenticated:
            client_unviewed_message = client_messages.filter(~Q(view_message__user_ks=request.user)).distinct().count()
            curator_unviewed_message = curator_messages.filter(~Q(view_message__user_ks=request.user)).distinct().count()

        else:
            client_unviewed_message = 1
            curator_unviewed_message = 2

        return JsonResponse(
            {
                'order': OrderSerializer(order).data,
                'client_chat': MessageSerializer(client_messages.all(), many=True).data,
                'curator_chat': MessageSerializer(curator_messages.all(), many=True).data,
                'chat': MessageSerializer(messages.all(), many=True).data,
                'user_id': 4,
                'unv_msg_client': client_unviewed_message,
                'unv_msg_curator': curator_unviewed_message,
                'room': room_name
            },
            safe=False
        )
    except Exception as ex:
        log_error(ex)
        return JsonResponse({'error': 'not found'}, status=404)


# изменяет заказ
def edit_order_view(request: HttpRequest):
    if request.method != RequestMethod.POST:
        return JsonResponse({'error': 'request method must be POST'}, status=404)

    data = request.POST

    try:
        if data['type'] == EditOrderAction.EDIT_SOFT:
            order = Order.objects.filter(id=data['order_id'])
            order(soft_id=data['soft_id'])
            order.save()

        elif data['type'] == EditOrderAction.ADD_CURATOR:
            OrderCurator.objects.create(user_id=data['user_id'], order_id=data['order_id'])

        elif data['type'] == EditOrderAction.EDIT_SOFT:
            OrderCurator.objects.filter(user_id=data['user_id'], order_id=data['order_id']).delete()

        else:
            return JsonResponse({'error': 'type action not found'}, status=401)

        return JsonResponse({'message': 'successful'}, status=200)

    except Exception as ex:
        return JsonResponse({'error': ex}, status=401)


# отмечает сообщения просмотренными
def viewed_msg_view(request: HttpRequest):
    if request.method != RequestMethod.POST:
        return JsonResponse({'error': 'request method must be POST'}, status=404)

    data = request.POST

    try:
        unviewed_messages = Message.objects.filter(
            user_id=data['user_id'],
            order_id=data['order_id'],
            chat=data['chat'],
            view_message__user_ks__isnull=True
        ).distinct().all()

        for msg in unviewed_messages:
            ViewMessage.objects.create(message=msg, user_ks_id=data['user_id'])

        return JsonResponse({'message': 'successful'}, status=200)

    except Exception as ex:
        return JsonResponse({'error': ex}, status=401)
