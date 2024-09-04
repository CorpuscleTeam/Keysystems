import logging

from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json

from . import curator_utils as utils
from common.models import OrderTopic, Notice, Order, Soft, UserKS, OrderCurator
from common.serializers import NoticeSerializer, SimpleOrderSerializer, SimpleWithCurOrderSerializer, UserKSSerializer
import common as ut
from enums import RequestMethod, OrderStatus, notices_dict, ChatType


# мои задачи
def cur_index_1_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    # orders = utils.get_orders_curator(request)

    orders = OrderCurator.objects.select_related('order').filter(user=request.user).order_by('order__created_at').all()
    order_list = [order_curator.order for order_curator in orders]
    logging.warning(f'order_list: {len(order_list)}')

    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'main_data': curator_data,
        # 'orders': utils.get_orders_curator(request, for_user=True),
        'orders': json.dumps(SimpleOrderSerializer(order_list, many=True).data),
    }
    return render(request, 'curator/cur_index_1_1.html', context)


# общие задачи
def cur_index_2_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    inn_selected = None
    cur_selected = None
    dist_selected = None
    soft_selected = None
    sort = None

    orders = utils.get_orders_curator(request)
    curators = UserKS.objects.filter(is_staff=True)

    filters = {
        'inn_list': list(set(order.customer.inn for order in orders)),
        'inn_selected': inn_selected,
        'cur_list': list(set(curator.full_name for curator in curators)),
        'cur_selected': cur_selected,
        'dist_list': list(set(order.customer.district.title for order in orders)),
        'dist_selected': dist_selected,
        'soft_list': list(set(order.soft.title for order in orders)),
        'soft_selected': soft_selected,
        'sort': sort,
    }

    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'filters': json.dumps(filters),
        'main_data': curator_data,
        # 'orders': json.dumps(SimpleOrderSerializer(orders, many=True).data),
        'orders': json.dumps(SimpleWithCurOrderSerializer(orders, many=True).data),
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

    if request.user.is_authenticated:
        # обнуляем непросмотренные уведомления
        Notice.objects.filter(user_ks=request.user, viewed=False).update(viewed=True)

    curator_data = utils.get_main_curator_front_data(request)
    context = {
        'main_data': curator_data,
        'notices': json.dumps(NoticeSerializer(notices, many=True).data),
    }
    return render(request, 'curator/cur_index_3.html', context)
