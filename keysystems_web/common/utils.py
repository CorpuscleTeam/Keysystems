from random import choice
from datetime import datetime, timedelta

from .data import months_str_ru



def pass_gen(len_: int = 8) -> str:
    return ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(len_)])


#     СЕГОДНЯ / 11:02
# 18 февраля 2024 / 6:32
# возвращает текстовые дата и время
def get_data_string(dt: datetime) -> str:
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    if dt.date() == today:
        data_str = 'СЕГОДНЯ'
    elif dt.date() == yesterday:
        data_str = 'ВЧЕРА'
    else:
        data_str = f'{dt.day} {months_str_ru.get(dt.month)} {dt.year}'

    return f'{data_str} / {dt.hour}:{dt.minute}'



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
