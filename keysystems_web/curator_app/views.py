from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE
from common.models import OrderTopic, Notice, Order, Soft
from common.serializers import OrderSerializer
import common as ut
from enums import RequestMethod, OrderStatus, notices_dict


# удалить аналог 2_2
def cur_index_1_1(request: HttpRequest):
    context = {
        'main_data': {
            'inn': 1234567890,
            'fio': 'Тестов Тест Тестович',
            'orders_count': 3,
            'notice': 6
        }
    }
    return render(request, 'curator/cur_index_1_1.html', context)


# удалить аналог 2_2
def cur_index_2_1(request: HttpRequest):
    context = {
        'main_data': {
            'inn': 1234567890,
            'fio': 'Тестов Тест Тестович',
            'orders_count': 3,
            'notice': 6
        }
    }
    return render(request, 'curator/cur_index_2_1.html', context)


# удалить аналог 2_2
def cur_index_3(request: HttpRequest):
    context = {
        'main_data': {
            'inn': 1234567890,
            'fio': 'Тестов Тест Тестович',
            'orders_count': 3,
            'notice': 6
        }
    }
    return render(request, 'curator/cur_index_3.html', context)
