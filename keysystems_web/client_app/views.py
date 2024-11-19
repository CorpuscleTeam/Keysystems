from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.db.models import Prefetch

from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE
from .forms import OrderForm
from common.logs import log_error
from .models import News, FAQ, UpdateSoft, UpdateSoftFiles, ViewUpdate
from . import client_utils as utils
from .serializers import NewsSerializer, UpdateSoftSerializer
from common.models import Notice, Order, Soft, OrderCurator
from common.serializers import SimpleOrderSerializer, NoticeSerializer
import common as ut
from enums import RequestMethod, OrderStatus, soft_dict


# страничка с новостями
def index_4_1(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_4_1')

    news = News.objects.filter(is_active=True).order_by('-created_at').all()

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'news': json.dumps(NewsSerializer(news, many=True).data),
    }
    return render(request, 'client/index_4_1.html', context)


# новость подробно
def index_4_2(request: HttpRequest, news_id: int):
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_4_2')

    # news_id = request.GET.get('news', 1)
    main_news = News.objects.get(pk=news_id)
    # news_json = serialize(format='json', queryset=[main_news])
    # news_data = json.loads(news_json)
    #
    # created_at = news_data[0]['fields']['created_at']
    # created_at_date = datetime.fromisoformat(created_at)  # Преобразуем строку в объект datetime
    # news_data[0]['fields']['day'] = created_at_date.day
    # news_data[0]['fields']['month'] = ut.months_str_ru.get(created_at_date.month, '')
    # news_data[0]['fields']['year'] = created_at_date.year
    #
    # news_json = json.dumps(news_data[0])

    # Получение предыдущей записи того же типа
    previous_news = News.objects.filter(
        created_at__lt=main_news.created_at
    ).order_by('-created_at').first()

    # Получение следующей записи того же типа
    next_news = News.objects.filter(
        created_at__gt=main_news.created_at
    ).order_by('created_at').first()

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        # 'news': serialize(format='json', queryset=[main_news]),
        'news': json.dumps(NewsSerializer(main_news).data),
        'news_raw': main_news,
        'previous_news': previous_news.id if previous_news else 0,
        'next_news': next_news.id if next_news else 0,
    }
    return render(request, 'client/index_4_2.html', context)


# заявки
def index_5_1(request: HttpRequest):

    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        # log_error(f'5_1 post {request.POST}', wt=False)
        utils.form_processing(request)
        return redirect('index_5_1')

    orders = Order.objects.filter(from_user=request.user).order_by('created_at')
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'orders': json.dumps(SimpleOrderSerializer(orders, many=True).data)
    }
    return render(request, 'client/index_5_1.html', context)


# уведомления
def index_6(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_6')

    notices = Notice.objects.filter(user_ks=request.user).order_by('-created_at').all()
    # обнуляем непросмотренные уведомления
    Notice.objects.filter(user_ks=request.user, viewed=False).update(viewed=True)

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'notices': json.dumps(NoticeSerializer(notices, many=True).data)
    }
    return render(request, 'client/index_6.html', context)


# обновление списком
def index_7_1(request: HttpRequest):
    log_error(f'>> index_7_1 {request.GET}', wt=False)
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_7_1')
    # updates = UpdateSoft.objects.select_related('soft').prefetch_related('files').filter(is_active=True).order_by('-created_at').all()
    updates = UpdateSoft.objects.filter(is_active=True).order_by('-created_at').all()

    # tst =OrderSerializer(updates)

    # updates_json = []
    # for update in updates:
    #     files = UpdateSoftFiles.objects.filter(update_soft=update.pk).all()
    #     update_files = []
    #     for file in files:
    #         update_files.append({'url': f'..{file.file.url}', 'name': file.file.name})
    #         # update_files.append(file.file.value)
    #
    #     updates_json.append(
    #         {
    #             'pk': update.pk,
    #             'date': ut.get_date_string(update.created_at),
    #             # 'soft': update.soft.title,
    #             'soft': soft_dict.get(update.soft, 'н/д'),
    #             'description': update.description,
    #             'update_files': update_files
    #         }
    #     )
    #     ut.log_error(updates_json, wt=False)

    client_data = utils.get_main_client_front_data(request)

    # записываем просмотренные обновления и обнуляем счётчик для фронта
    if client_data.get('unviewed_updates'):
        for update in client_data['unviewed_updates']:
            ViewUpdate.objects.create(
                update_soft=update,
                user_ks=request.user
            )
        client_data['update_count'] = 0

    context = {
        **client_data,
        'update_json': json.dumps(UpdateSoftSerializer(updates, many=True).data)
    }
    return render(request, 'client/index_7_1.html', context)


# обновление подробнее
def index_7_2(request: HttpRequest, update_id: int):
    # log_error(f'>> index_7_2 {update_id} {type(update_id)}', wt=False)

    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_7_2')

    # update_id = request.GET.get('update', 1)
    update = UpdateSoft.objects.filter(id=update_id).order_by('-created_at').first()

    # files = UpdateSoftFiles.objects.filter(update_soft=update.pk).all()
    # update_files = []
    # for file in files:
    #     file_name = file.file.name.split('/')[-1]
    #     file_type = file_name[-3:] if file_name[-3:] in ut.upload_file_type else 'file'
    #     update_files.append({
    #         'url': f'/{file.file.url}',
    #         'name': file_name,
    #         'size': ut.get_size_file_str(file.file_size),
    #         'icon': f"/{os.path.join('static', 'site', 'img', 'files', f'{file_type}.svg')}",
    #     })
    #
    # update_json = {
    #     'date': ut.get_date_string(update.created_at),
    #     'soft': soft_dict.get(update.soft),
    #     'description': update.description,
    #     'update_files': update_files
    #     }
    #
    # ut.log_dict(update_json)
    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'update_json': json.dumps(UpdateSoftSerializer(update).data)
    }
    return render(request, 'client/index_7_2.html', context)


# FAQ частозадаваемые
def index_8(request: HttpRequest):
    if utils.is_access_denied(request):
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        utils.form_processing(request)
        return redirect('index_8')

    faq = FAQ.objects.filter(is_active=True).order_by('-created_at').all()

    client_data = utils.get_main_client_front_data(request)
    context = {
        **client_data,
        'faq': serialize(format='json', queryset=faq)
    }
    return render(request, 'client/index_8.html', context)
