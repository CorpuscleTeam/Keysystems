from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json

from . import curator_utils as utils
from common.models import OrderTopic, Notice, Order, Soft
from common.serializers import NoticeSerializer
import common as ut
from enums import RequestMethod, OrderStatus, notices_dict


# мои задачи
def cur_index_1_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'main_data': curator_data,
        'orders': utils.get_orders_curator(request, for_user=True)
    }
    return render(request, 'curator/cur_index_1_1.html', context)


# общие задачи
def cur_index_2_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'main_data': curator_data,
        'orders': utils.get_orders_curator(request),
        'order_all_data': 1
    }
    return render(request, 'curator/cur_index_2_1.html', context)


# уведомления
def cur_index_3(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.user.is_authenticated:
        notices = Notice.objects.filter(user_ks=request.user).order_by('-created_at').all()
    else:
        notices = Notice.objects.filter().order_by('-created_at').all()

    notice = NoticeSerializer(notices)

    if request.user.is_authenticated:
    # обнуляем непросмотренные уведомления
        Notice.objects.filter(user_ks=request.user, viewed=False).update(viewed=True)
    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'main_data': curator_data,
        'notices': notice.serialize()
    }
    return render(request, 'curator/cur_index_3.html', context)
