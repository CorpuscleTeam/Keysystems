from random import choice
from datetime import datetime, timedelta
from django.http import HttpRequest
from urllib.parse import urlparse

import os

from .data import months_str_ru, upload_file_type
from .logs import log_error


def pass_gen(len_: int = 8) -> str:
    return ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len_)])


#     СЕГОДНЯ / 11:02
# 18 февраля 2024 / 6:32
# возвращает текстовые дата и время
def get_date_string(dt: datetime) -> str:
    now = datetime.now()
    yesterday = now - timedelta(days=1)
    if dt.date() == now.date():
        data_str = 'СЕГОДНЯ'
    elif dt.date() == yesterday.date():
        data_str = 'ВЧЕРА'
    else:
        data_str = f'{dt.day} {months_str_ru.get(dt.month)} {dt.year}'

    # log_error(f'{dt} | {dt.hour} {dt.hour < 10} | {dt.minute} {dt.minute < 10}', wt=False)
    hour_str = dt.hour if dt.hour >= 10 else f'0{dt.hour}'
    minute_str = dt.minute if dt.minute > 10 else f'0{dt.minute}'
    return f'{data_str} / {hour_str}:{minute_str}'


# возвращает время для сообщений
def get_time_string(dt: datetime) -> str:
    hour_str = dt.hour if dt.hour > 10 else f'0{dt.hour}'
    minute_str = dt.minute if dt.minute > 10 else f'0{dt.minute}'
    return f'{hour_str}:{minute_str}'


# Создаёт строку с размером файла
def get_size_file_str(size: int) -> str:
    for unit in ['байт', 'КБ', 'МБ', 'ГБ']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


# возвращает ссылку на иконку файла
def get_file_icon_link(file_name: str) -> str:
    file_type = file_name[-3:] if file_name[-3:] in upload_file_type else 'file'
    return f"../{os.path.join('static', 'site', 'img', 'files', f'{file_type}.svg')}"


# возвращает url текущей страницы
def get_current_url(request: HttpRequest) -> str:
    referer = request.META.get('HTTP_HOST', '')
    log_error(f'referer: {referer}', wt=False)
    if referer:
        parsed_url = urlparse(referer)
        return f"{parsed_url.scheme}://{parsed_url.netloc}"


# Получить ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Получить юзерагент
def get_user_agent(request):
    user_agent = request.META.get('HTTP_USER_AGENT')
    return user_agent
