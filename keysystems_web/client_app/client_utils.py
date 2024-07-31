from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.utils.text import get_valid_filename
from django.db.models import Count, Q
from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE, DEBUG
from .forms import OrderForm, UserSettingForm
from .models import News, ViewNews, UpdateSoft
from common.models import OrderTopic, Soft, Order, DownloadedFile, Notice, UsedSoft
from common import log_error, months_str_ru
from enums import OrderStatus, FormType


# проверяет доступ к странице
def is_access_denied(request: HttpRequest) -> bool:
    log_error(f'DEBUG: {DEBUG}', wt=False)
    if DEBUG:
        return False
    if request.user.is_authenticated and not request.user.is_staff:
        return False
    else:
        return True


# Собирает данные для стандартного окружения клиентской части
def get_main_client_front_data(request: HttpRequest) -> dict:
    soft_json = serialize(format='json', queryset=Soft.objects.filter(is_active=True).all())
    topics_json = serialize(format='json', queryset=OrderTopic.objects.filter(is_active=True).all())

    if request.user.is_authenticated:
        # количество заявок
        user_orders_count = Order.objects.filter(from_user=request.user).exclude(status=OrderStatus.DONE).count()
        # количество непросмотренных уведомлений
        notice_count = Notice.objects.filter(viewed=False, user_ks=request.user).count()
        # Получаем все объекты UpdateSoft, которые пользователь не просмотрел
        unviewed_updates = UpdateSoft.objects.filter(~Q(view_update__user_ks=request.user)).distinct()
        # Считаем количество непросмотренных обновлений
        unviewed_updates_count = unviewed_updates.count()
        # используемый софт
        used_soft = UsedSoft.objects.get(user=request.user)

        log_error(f'>>>> {request.user.customer.inn}', wt=False)

        return {
            'topics': topics_json,
            'soft': soft_json,
            'orders_count': user_orders_count,
            'notice': notice_count,
            'update_count': unviewed_updates_count,
            'unviewed_updates': unviewed_updates,
            'main_data': json.dumps(
                {
                    'inn': request.user.customer.inn,
                    'institution': request.user.customer.title,
                    'region': request.user.customer.district.title,
                    'email': request.user.username,
                    'full_name': request.user.full_name,
                    'used_soft': used_soft.id,
                    'phone': request.user.phone,
                }
            )
        }
    else:
        return {
            'topics': topics_json,
            'soft': soft_json,
            'orders_count': 2,
            'notice': 3,
            'update_count': 12,
            'main_data': json.dumps(
                {
                    'inn': "1234567890",
                    'institution': "OOO Oooo",
                    'region': 'ChO',
                    'email': 'ex@mail.com',
                    'full_name': 'Мурат Насырович Шлакоблокунь',
                    'used_soft': 2,
                    'phone': '79012345678',
                }
            )
        }


# >>>> <QueryDict: {'csrfmiddlewaretoken': ['pYTOAQritYwXPWYtFZ11WJiIYZOY2Dei7EnijgTOLqaDbg5dfuTEHWeM9poMfXnP'],
# 'type_form': ['order'], 'type_appeal': ['1'], 'type_soft': ['1'], 'description': [''], 'addfile': ['']}>


def form_processing(request: HttpRequest) -> None:
    log_error(f'>>>> {request.POST}', wt=False)

    type_form = request.POST.get('type_form')
    if type_form == FormType.ORDER:
        form = OrderForm(request.POST, request.FILES)
        # log_error(f'>>>> form.is_valid(): {form.is_valid()}\n{form.errors}\n{form.data}', wt=False)
        if form.is_valid():
            soft = Soft.objects.get(pk=form.cleaned_data['type_soft'])
            topic = OrderTopic.objects.get(pk=form.cleaned_data['type_soft'])
            new_order = Order(
                from_user=request.user,
                text=form.cleaned_data['description'],
                soft=soft,
                topic=topic,
                customer=request.user.customer
            )
            new_order.save()

            files = request.FILES.getlist('addfile')

            folder_path = os.path.join(FILE_STORAGE, str(request.user.customer.inn), str(new_order.pk))
            # folder_path = os.path.join(FILE_STORAGE, str(request.user.customer.inn), 'test')
            if not os.path.exists(folder_path) and files:
                os.makedirs(folder_path)

            fs = FileSystemStorage(location=folder_path)  # Устанавливаем локальное хранилище для указанной папки
            for uploaded_file in files:
                file_name = get_valid_filename(uploaded_file.name)

                # Сохраняем файл
                filename = fs.save(file_name, uploaded_file)  # Используем только имя файла
                file_url = fs.url(filename)  # Получаем URL файла

                DownloadedFile.objects.create(
                    user_ks=request.user,
                    order=new_order,
                    url=file_url
                )

    elif type_form == FormType.SETTING:
        form = UserSettingForm(request.POST)
        # log_error(f'>>>> form.is_valid(): {form.is_valid()}\n{form.errors}\n{form.data}', wt=False)
        if not form.is_valid():
            return

        user = request.user
        user.username = form.cleaned_data['settings_email']
        user.full_name = form.cleaned_data['settings_responsible']
        user.phone = form.cleaned_data['settings_phone']
        user.save()

        soft = Soft.objects.get(id=form.cleaned_data['type_soft'])
        used_soft = UsedSoft.objects.get(user=user)
        used_soft.soft = soft
        used_soft.save()
        log_error(f'>>>> save user', wt=False)


# >>>> <QueryDict: {'csrfmiddlewaretoken': ['iM47xrP89HK7Rr7igTlGndSKF9jr2u4j0syBgRhEr9oNdLe2Qodj8qOOQzTffOdQ'],
# 'type_form': ['setting'], 'settings_inn': ['1234'], 'settings_name': ['Наименование чреждение'],
# 'settings_reg': ['Челябинская область'],
# 'type_soft': ['1'], 'settings_email': [''], 'settings_responsible': [''], 'settings_phone': ['']}>
# изменение данных пользователя