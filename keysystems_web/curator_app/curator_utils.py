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
from common.models import OrderTopic, Soft, Order, DownloadedFile, Notice, UsedSoft, UserKS, OrderCurator
from common.serializers import FullOrderSerializer, SimpleOrderSerializer
from common import log_error, months_str_ru
from enums import OrderStatus, FormType


# проверяет доступ к странице куратора
def is_access_denied(request: HttpRequest) -> bool:
    if DEBUG:
        if not request.user.is_authenticated or not request.user.is_staff:
            user = UserKS.objects.filter(is_staff=True).order_by('?').first()
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
        user_orders_count = (OrderCurator.objects.select_related('order').filter(user=request.user).
                             exclude(order__status=OrderStatus.DONE).order_by('order__created_at').count())

        # количество непросмотренных уведомлений
        notice_count = Notice.objects.filter(viewed=False, user_ks=request.user).count()
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
def get_orders_curator(request: HttpRequest, for_user: bool = False):
    orders = Order.objects.order_by('-created_at')

    return orders.all()
    # return json.dumps(SimpleOrderSerializer(orders.all(), many=True).data)
