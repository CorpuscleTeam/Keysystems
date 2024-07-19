from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE
from .forms import OrderForm
from .models import News
from common.models import OrderTopic, Soft, Order, DownloadedFile
from common import log_error, months_str_ru
from enums import OrderStatus


# Собирает данные для стандартного окружения клиентской части
def get_main_client_front_data(request: HttpRequest) -> dict:
    user_orders_count = Order.objects.filter(
        from_user=request.user.pk
    ).exclude(
        status=OrderStatus.DONE
    ).count()

    soft_json = serialize(format='json', queryset=Soft.objects.filter(is_active=True).all())
    topics_json = serialize(format='json', queryset=OrderTopic.objects.filter(is_active=True).all())
    news = News.objects.filter(is_active=True).all()
    news_json = serialize(format='json', queryset=news)

    news_data = json.loads(news_json)

    for item in news_data:
        created_at = item['fields']['created_at']
        created_at_date = datetime.fromisoformat(created_at)  # Преобразуем строку в объект datetime
        item['fields']['day'] = created_at_date.day
        item['fields']['month'] = months_str_ru.get(created_at_date.month, '')
        item['fields']['year'] = created_at_date.year
        log_error(f">>>> {item['fields']['day']} {item['fields']['month']} {item['fields']['year']}", wt=False)

    news_json = json.dumps(news_data)  # Преобразуем обратно в JSON
    log_error(request.user.inn, wt=False)
    return {
        'news': news_json,
        'topics': topics_json,
        'soft': soft_json,
        'inn': request.user.inn,
        'orders_count': user_orders_count,
        'notice': 10,
        'update_count': 44,
    }


# сохраняет форму отправки обращения
def order_form_processing(request: HttpRequest, form: OrderForm):
    soft = Soft.objects.get(pk=form.cleaned_data['type_soft'])
    topic = OrderTopic.objects.get(pk=form.cleaned_data['type_soft'])
    new_order = Order(
        from_user=request.user,
        text=form.cleaned_data['description'],
        soft=soft,
        topic=topic
    )
    new_order.save()

    files = request.FILES.getlist('addfile')

    folder_path = os.path.join(FILE_STORAGE, str(request.user.inn), str(new_order.pk))
    if not os.path.exists(folder_path) and files:
        os.mkdir(folder_path)

    fs = FileSystemStorage()
    for uploaded_file in files:
        file_path = os.path.join(folder_path, uploaded_file.name)
        filename = fs.save(file_path, uploaded_file)
        file_url = fs.url(filename)

        DownloadedFile.objects.create(
            user_ks=request.user,
            order=new_order,
            url=file_url
        )

