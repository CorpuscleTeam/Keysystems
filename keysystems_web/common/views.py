from django.http import JsonResponse, HttpRequest
from django.db.models import Count, Q, Case, When, IntegerField
from django.shortcuts import render

import json
import os
import csv
import logging

from keysystems_web.settings import BASE_DIR
from .models import Order, Message, OrderCurator, ViewMessage, UserKS, Soft, Customer, Ministry
from . import models as m
from .serializers import FullOrderSerializer, MessageSerializer, UserKSSerializer
from .logs import log_error
from .data import client_data
from enums import ChatType, RequestMethod, EditOrderAction, soft_list_dict, CustomerType


# полные данные по заказу
def get_order_data(request: HttpRequest, order_id):
    # log_error('>>>>>>>>>>>>', wt=False)
    try:
        # log_error(f'{order_id}', wt=False)

        order = Order.objects.filter(id=order_id).first()
        messages = Message.objects.prefetch_related('view_message').filter(order=order).order_by('created_at')

        # разделяем чаты на клиентский и кураторский
        client_messages = messages.filter(chat=ChatType.CLIENT.value)
        curator_messages = messages.filter(chat=ChatType.CURATOR.value)

        room_name = f'order{order_id}'

        # получаем непросмотренные сообщения
        # Все сообщения для указанного заказа с необходимыми предвыборками
        messages = Message.objects.prefetch_related('view_message').filter(order=order)

        # Фильтрация сообщений, которые не от текущего пользователя
        non_user_messages = messages.exclude(from_user=request.user)

        # Используем аннотации для подсчета непросмотренных сообщений
        annotated_messages = non_user_messages.annotate(
            is_unviewed_by_user=Case(
                When(~Q(view_message__user_ks=request.user), then=1),
                default=0,
                output_field=IntegerField()
            )
        )

        # Подсчет непросмотренных клиентских сообщений
        client_unviewed_message = annotated_messages.filter(
            chat=ChatType.CLIENT.value,
            is_unviewed_by_user=1
        ).distinct().count()

        # Подсчет непросмотренных кураторских сообщений
        curator_unviewed_message = annotated_messages.filter(
            chat=ChatType.CURATOR.value,
            is_unviewed_by_user=1
        ).distinct().count()

        user_id = request.user.id

        return JsonResponse(
            {
                'order': FullOrderSerializer(order).data,
                'client_chat': MessageSerializer(client_messages.all(), many=True).data,
                'curator_chat': MessageSerializer(curator_messages.all(), many=True).data,
                'chat': MessageSerializer(messages.all(), many=True).data,
                'user_id': user_id,
                'unv_msg_client': client_unviewed_message,
                'unv_msg_curator': curator_unviewed_message,
                'room': room_name,
                # 'soft': json.dumps(soft_list_dict),
                'soft': soft_list_dict,
            },
            safe=False
        )
        
    except Exception as ex:
        log_error(ex)
        return JsonResponse({'error': 'not found'}, status=404)


# изменяет заказ (скорее всего удалить)
def edit_order_view(request: HttpRequest):
    if request.method != RequestMethod.POST:
        return JsonResponse({'error': 'request method must be POST'}, status=404)

    data = request.POST

    try:
        # if data['type'] == EditOrderAction.EDIT_SOFT:
        #     order = Order.objects.filter(id=data['order_id'])
        #     order(soft_id=data['soft_id'])
        #     order.save()

        if data['type'] == EditOrderAction.ADD_CURATOR:
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


# отправляет список кураторов
def get_curator_view(request: HttpRequest):
    if request.method != RequestMethod.POST:
        return JsonResponse({'error': 'request method must be POST'}, status=404)

    data: dict = json.loads(request.body)
    log_error(f'fdata: {type(data)} {data}', wt=False)
    try:
        order_id = int(data.get('order_id', 0))
        # curators = UserKS.objects.filter(is_staff=True).all()
        # log_error(f'len(curators): {len(curators)} ', wt=False)
        curators = UserKS.objects.filter(is_staff=True).exclude(
            id__in=OrderCurator.objects.filter(order_id=order_id).values('user_id')
        )

        # order_curators = OrderCurator.objects.filter(order_id=order_id).select_related('user').all()
        # logging.warning('order_curators')
        # for cur in order_curators:
        #     logging.warning(cur.user.full_name)

        return JsonResponse(UserKSSerializer(curators, many=True).data, status=200, safe=False)

    except Exception as ex:
        log_error(ex)
        return JsonResponse({'error': str(ex)}, status=401, safe=False)


def edit_order_soft_view(request: HttpRequest):
    log_error('edit_order_soft', wt=False)
    # Получаем параметры из GET-запроса
    selected_option = request.GET.get('option')
    order_id = request.GET.get('order_id')

    # Логика обработки данных (например, можно обновить объект или вернуть данные)
    # Пример: Обрабатываем данные или сохраняем изменения в базе данных

    # Возвращаем JSON-ответ
    response_data = {
        'status': 'success',
        'message': f'Вы выбрали вариант {selected_option} для заказа {order_id}'
    }
    return JsonResponse(response_data)
