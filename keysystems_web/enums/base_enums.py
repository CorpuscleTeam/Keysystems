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
        (OrderStatus.DONE.value, 'Выполнено'),
)


class FormType(str, Enum):
    ORDER = 'order'
    SETTING = 'setting'


class ChatType(str, Enum):
    CLIENT = 'client'
    CURATOR = 'curator'


CHAT_CHOICES = (
        (ChatType.CLIENT.value, 'С клиентом'),
        (ChatType.CURATOR.value, 'Кураторский')
)


class MsgType(str, Enum):
    MSG = 'msg'
    FILE = 'file'


MSG_TYPE_CHOICES = (
        (MsgType.MSG.value, 'Сообщение'),
        (MsgType.FILE.value, 'Файл')
)


# уведомления
class NoticeType(str, Enum):
    ORDER_ACTIVE = 'order_active'
    ORDER_DONE = 'order_done'
    NEW_MSG = 'NEW_MSG'


notices_dict = {
    NoticeType.ORDER_ACTIVE.value: 'Ваша задача #{pk:05d} переведена в статус «В РАБОТЕ».',
    NoticeType.ORDER_DONE.value: 'Ваша задача #{pk:05d} переведена в статус «ВЫПОЛНЕНО».',
    NoticeType.NEW_MSG.value: 'В заявке #{pk:05d} куратор оставил новое сообщение.',
}

notices_tuple = ((k, v) for k, v in notices_dict.items())


# изменения заказа
class EditOrderAction(str, Enum):
    MSG = 'msg'
    EDIT_SOFT = 'edit_soft'
    EDIT_CURATOR = 'edit_curator'
    ADD_CURATOR = 'add_curator'
    DEL_CURATOR = 'del_curator'
