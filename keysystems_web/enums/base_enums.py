from enum import Enum


class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'


class UserRole(str, Enum):
    CLIENT = 'client'
    STAFF = 'staff'


class OrderStatus(str, Enum):
    NEW = 'new'
    ACTIVE = 'active'
    DONE = 'done'


ORDER_CHOICES = (
        (OrderStatus.NEW.value, 'Новый'),
        (OrderStatus.ACTIVE.value, 'В работе'),
        (OrderStatus.DONE.value, 'Активный'),
)


class NewsEntryType(str, Enum):
    NEWS = 'news'
    UPDATE = 'update'


ENTRY_TYPES = (
    (NewsEntryType.NEWS.value, 'Новость'),
    (NewsEntryType.UPDATE.value, 'Обновление ПО')
)


# уведомления
class Notice(str, Enum):
    ORDER_ACTIVE = 'order_active'
    ORDER_DONE = 'order_done'
    NEW_MSG = 'NEW_MSG'


notices_dict = {
    Notice.ORDER_ACTIVE.value: 'Ваша задача #{pk} переведена в статус «В РАБОТЕ».',
    Notice.ORDER_DONE.value: 'Ваша задача #{pk} переведена в статус «ВЫПОЛНЕНО». Оцените качество выполненной работы.',
    Notice.NEW_MSG.value: 'В заявке #{pk} куратор оставил новое сообщение.',
}

notices_tuple = ((k, v) for k, v in notices_dict.items())