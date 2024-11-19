import logging

from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json
import random

from . import curator_utils as utils
from common.models import Notice, Order, Soft, UserKS, OrderCurator
from common.serializers import NoticeSerializer, SimpleOrderSerializer, SimpleWithCurOrderSerializer, UserKSSerializer
from common.logs import log_error
import common as ut
from enums import RequestMethod, OrderStatus, notices_dict, ChatType, soft_dict


# мои задачи
def cur_index_1_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    # logging.warning(f'request.user: {request.user.full_name} {request.user.id}')
    orders = OrderCurator.objects.select_related('order').filter(user=request.user).order_by('order__created_at').all()

    # order_list = [order_curator.order for order_curator in orders if order_curator.order]
    order_list = []
    added_orders = []  # Чтоб не задваивались заказы при ошибке записи
    for order_curator in orders:
        if order_curator.order.id not in added_orders:
            # logging.warning(f'{order_curator.order.id} - {added_orders}')
            order_list.append(order_curator.order)
            added_orders.append(order_curator.order.id)

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

    filter_dict = {}
    if request.method == RequestMethod.POST:
        filter_dict = request.POST
        # logging.warning(f'2_1 request.POST: {request.POST}')
        # logging.warning(f'2_1 request.POST: {type(request.POST)}')

    orders = utils.get_orders_curator(request, filter_dict)
    # log_error(f'filter_dict: {filter_dict}', wt=False)
    # log_error(f'orders: {len(orders)}', wt=False)
    curators = UserKS.objects.filter(is_staff=True)

    filters = {
        'orders': json.dumps(SimpleOrderSerializer(orders, many=True).data),
        'inn_list': list(set(order.customer.inn for order in orders)),
        'inn_selected': filter_dict.get('inn_filter'),
        'cur_list': list(set(curator.full_name for curator in curators)),
        # 'cur_selected': random.choice(list(set(curator.full_name for curator in curators))),
        'cur_selected': filter_dict.get('curator_filter'),
        # 'dist_list': list(set(order.customer.district.title for order in orders)),
        'dist_list': [],
        'dist_selected': filter_dict.get('district_filter'),
        # 'soft_list': list(set(order.soft.title for order in orders)),
        'soft_list': list(set(soft_dict.get(order.soft, 'н/д') for order in orders)),
        'soft_selected': filter_dict.get('soft_filter'),
        'sort': filter_dict.get('sort'),
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
