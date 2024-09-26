import logging

from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.utils.text import get_valid_filename
from django.db.models import Count, Q
from django.contrib.auth import login
from datetime import datetime

import os
import json

from keysystems_web.settings import FILE_STORAGE, DEBUG
from .forms import OrderForm, UserSettingForm
from .models import UpdateSoft
from common import models as m
from common import log_error, months_str_ru
import enums as e


# проверяет доступ к странице
def is_access_denied(request: HttpRequest) -> bool:
    if DEBUG:
        if not request.user.is_authenticated or request.user.is_staff:
            user = m.UserKS.objects.filter(is_staff=False).order_by('?').first()
            login(request, user)
        return False
    if request.user.is_authenticated and not request.user.is_staff:
        return False
    else:
        return True


# Собирает данные для стандартного окружения клиентской части
def get_main_client_front_data(request: HttpRequest) -> dict:
    soft_json = json.dumps(e.soft_list_dict)
    topics_json = json.dumps(e.order_topic_list_dict)

    # количество заявок
    user_orders_count = m.Order.objects.filter(from_user=request.user).exclude(status=e.OrderStatus.DONE).count()
    # количество непросмотренных уведомлений
    notice_count = m.Notice.objects.filter(viewed=False, user_ks=request.user).count()
    # Получаем все объекты UpdateSoft, которые пользователь не просмотрел
    unviewed_updates = UpdateSoft.objects.filter(~Q(view_update__user_ks=request.user)).distinct()
    # Считаем количество непросмотренных обновлений
    unviewed_updates_count = unviewed_updates.count()
    # используемый софт
    used_soft = m.UsedSoft.objects.get(user=request.user)

    # log_error(f'>>>> {request.user.customer.inn}', wt=False)

    return {
        'topics': topics_json,
        'soft': soft_json,
        'orders_count': user_orders_count,
        'notice': notice_count,
        'update_count': unviewed_updates_count,
        'unviewed_updates': unviewed_updates,
        'main_data': json.dumps(
            {
                'user_id': request.user.id,
                'inn': request.user.customer.inn,
                'institution': request.user.customer.title,
                'region': request.user.customer.district.title,
                'email': request.user.username,
                'full_name': request.user.full_name,
                'used_soft': used_soft.id,
                'phone': request.user.phone,
                'topics': topics_json,
                'soft': soft_json,
                'orders_count': user_orders_count,
                'notice': notice_count,
                'update_count': unviewed_updates_count,
                'unviewed_updates': unviewed_updates.count(),
            }
        )
    }


# >>>> <QueryDict: {'csrfmiddlewaretoken': ['pYTOAQritYwXPWYtFZ11WJiIYZOY2Dei7EnijgTOLqaDbg5dfuTEHWeM9poMfXnP'],
# 'type_form': ['order'], 'type_appeal': ['1'], 'type_soft': ['1'], 'description': [''], 'addfile': ['']}>
# возвращает куратора
def get_order_curator(soft: str, prefix: str, customer_type: str) -> list[m.UserKS]:
    if soft == e.Soft.B_SMART:
        curators = m.SoftBSmart.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.ADMIN_D:
        curators = m.SoftAdminD.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.S_SMART:
        curators = m.SoftSSmart.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.P_SMART:
        curators = m.SoftPSmart.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.WEB_T:
        curators = m.SoftWebT.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.DIGIT_B:
        curators = m.SoftDigitB.objects.filter(prefix=prefix, type=customer_type).all()
    elif soft == e.Soft.O_SMART:
        curators = m.SoftOSmart.objects.filter(prefix=prefix, type=customer_type).all()
    else:
        curators = False

    return curators


def form_processing(request: HttpRequest) -> None:
    # log_error(f'>>>> {request.POST}', wt=False)

    type_form = request.POST.get('type_form')
    if type_form == e.FormType.ORDER:
        form = OrderForm(request.POST, request.FILES)
        # log_error(f'>>>> form.is_valid(): {form.is_valid()}\n{form.errors}\n{form.data}', wt=False)
        if form.is_valid():
            # log_error(f'>>>> form.cleaned_data: {form.cleaned_data}\n\n{e.order_topic_dict.get(1)}', wt=False)
            # создаёт заказ
            new_order = m.Order(
                from_user=request.user,
                text=form.cleaned_data['description'],
                soft=form.cleaned_data['type_soft'],
                topic=form.cleaned_data['type_appeal'],
                # soft=soft,
                # topic=topic,
                customer=request.user.customer
            )
            new_order.save()

            # добавляет куратора
            curators = get_order_curator(
                soft=form.cleaned_data['type_soft'],
                prefix=str(request.user.customer.inn)[:4],
                customer_type=request.user.customer.form_type
            )
            if curators:
                for curator in curators:
                    m.OrderCurator.objects.create(
                        user_id=curator.user_id,
                        order=new_order
                    )
            else:
                curator = m.UserKS.objects.filter(is_staff=True).order_by('?').first()
                m.OrderCurator.objects.create(
                    user_id=curator.id,
                    order=new_order
                )

            # Запись коммента
            full_description = form.cleaned_data.get('fullDescription')
            if full_description:
                m.Message.objects.create(
                    type_msg=e.MsgType.MSG.value,
                    from_user=request.user,
                    chat=e.ChatType.CLIENT.value,
                    order=new_order,
                    text=full_description
                )

            # order_curators = m.CuratorDist.objects.filter(soft=soft, district=request.user.customer.district).all()
            # for curator in order_curators:
            #     m.OrderCurator.objects.create(
            #         user=curator,
            #         order=new_order
            #     )

            #
            files = request.FILES.getlist('addfile')

            if not files:
                return

            folder_path = os.path.join(FILE_STORAGE, str(request.user.customer.inn), str(new_order.pk))
            if not os.path.exists(folder_path) and files:
                os.makedirs(folder_path)

            fs = FileSystemStorage(location=folder_path)  # Устанавливаем локальное хранилище для указанной папки
            for uploaded_file in files:
                file_name = get_valid_filename(uploaded_file.name)

                # Сохраняем файл
                fs.save(file_name, uploaded_file)  # Используем только имя файла
                file_url = os.path.join(folder_path, file_name).replace('/app', '')

                m.DownloadedFile.objects.create(
                    user_ks=request.user,
                    order=new_order,
                    url=file_url,
                    file_size=uploaded_file.size
                )

    elif type_form == e.FormType.SETTING:
        form = UserSettingForm(request.POST)

        if not form.is_valid():
            return

        log_error(f'>>>> form.cleaned_data: {form.cleaned_data}', wt=False)
        user = request.user
        user.username = form.cleaned_data['settings_email']
        user.full_name = form.cleaned_data['settings_responsible']
        user.phone = form.cleaned_data['settings_phone']
        user.save()

        # soft = m.Soft.objects.get(id=form.cleaned_data['type_soft'])
        used_soft = m.UsedSoft.objects.get(user=user)
        log_error(f'>>>> used_soft: {used_soft}', wt=False)
        used_soft.soft = form.cleaned_data['type_soft']
        # used_soft.soft = soft
        used_soft.save()
        # log_error(f'>>>> save user', wt=False)


# >>>> <QueryDict: {'csrfmiddlewaretoken': ['iM47xrP89HK7Rr7igTlGndSKF9jr2u4j0syBgRhEr9oNdLe2Qodj8qOOQzTffOdQ'],
# 'type_form': ['setting'], 'settings_inn': ['1234'], 'settings_name': ['Наименование чреждение'],
# 'settings_reg': ['Челябинская область'],
# 'type_soft': ['1'], 'settings_email': [''], 'settings_responsible': [''], 'settings_phone': ['']}>
# изменение данных пользователя