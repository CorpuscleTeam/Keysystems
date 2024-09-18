from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login
from django.core.serializers import serialize
from django.utils.text import get_valid_filename
from django.db.models import Count, Q
from datetime import datetime

import os
import json
import logging

from keysystems_web.settings import FILE_STORAGE, DEBUG
# from .forms import OrderForm, UserSettingForm
# from .models import News, ViewNews, UpdateSoft
from common import models as cm
from common.serializers import FullOrderSerializer, SimpleOrderSerializer
from common import log_error, months_str_ru
from enums import OrderStatus, FormType


# проверяет доступ к странице куратора
def is_access_denied(request: HttpRequest) -> bool:
    if DEBUG:
        if not request.user.is_authenticated or not request.user.is_staff:
            user = cm.UserKS.objects.filter(is_staff=True, is_superuser=False).order_by('?').first()
            login(request, user)
        return False
    if request.user.is_authenticated and request.user.is_staff:
        return False
    else:
        return True


# Собирает данные для стандартного окружения кураторской части
def get_main_curator_front_data(request: HttpRequest) -> str:
    if request.user.is_authenticated:
        # количество заявок
        # user_orders_count = Order.objects.filter().exclude(status=OrderStatus.DONE).count()
        user_orders_count = (cm.OrderCurator.objects.select_related('order').filter(user=request.user).
                             exclude(order__status=OrderStatus.DONE).order_by('order__created_at').count())

        # количество непросмотренных уведомлений
        notice_count = cm.Notice.objects.filter(viewed=False, user_ks=request.user).count()
        return json.dumps(
            {
                # 'inn': request.user.customer.inn,
                'inn': 1234567890,
                'fio': request.user.full_name,
                'orders_count': user_orders_count,
                'notice': notice_count
            }
        )
    else:
        return json.dumps(
            {
                'inn': 1234567890,
                'fio': 'Тестов Тест Тестович',
                'orders_count': 3,
                'notice': 6
            }
        )


# возвращае заказы по фильтрам
def get_orders_curator(request: HttpRequest, filters: dict):
    if filters.get('sort') == 'optionSort2':
        orders = cm.Order.objects.order_by('-created_at')
    else:
        orders = cm.Order.objects.order_by('created_at')

    if filters.get('inn_filter'):
        inn = int(filters.get('inn_filter'))
        customer = cm.Customer.objects.filter(inn=inn).first()
        orders.filter(customer=customer)

    if filters.get('curator_filter'):
        curator = cm.UserKS.objects.filter(full_name=filters.get('curator_filter')).first()
        orders.prefetch_related('order_curator').filter(order_curator__user=curator)

    if filters.get('district_filter'):
        district = cm.Customer.objects.filter(district=filters.get('district_filter')).first()
        orders.select_related('customer').filter(customer__district=district)

    if filters.get('soft_filter'):
        soft = cm.Soft.objects.filter(title=filters.get('soft_filter')).first()
        orders.filter(soft=soft)

    return orders.all()
    # return json.dumps(SimpleOrderSerializer(orders.all(), many=True).data)

'''
<QueryDict: {
'sort': ['optionSort1'], 
'inn_filter': ['1234567890'], 
'curator_filter': ['Вас Вася Васев'], 
'district_filter': ['Анабарский национальный (долгано-эвенкийский) район'], 
'soft_filter': ['ПО 2']}
'''
