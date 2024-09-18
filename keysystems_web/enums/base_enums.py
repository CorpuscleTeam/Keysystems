from enum import Enum


class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'


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
    FILE = 'file'
    EDIT_SOFT = 'edit_soft'
    EDIT_CURATOR = 'edit_curator'
    EDIT_STATUS = 'edit_status'
    VIEW_TAB = 'view_tab'

    ADD_CURATOR = 'add_curator'
    DEL_CURATOR = 'del_curator'


# вкладки
class TAB(str, Enum):
    TAB1 = '#tab1'
    TAB2 = '#tab2'
    TAB3 = '#tab3'


# темы обращения
class OrderTopic(str, Enum):
    TECH = 'tech'
    CONTRACT = 'contract'


order_topic_dict = {
    OrderTopic.TECH.value: 'Техническая проблема',
    OrderTopic.CONTRACT.value: 'Договорной отдел',
}

order_topic_list_dict = [
    {'id': OrderTopic.TECH.value, 'topic': 'Техническая проблема'},
    {'id': OrderTopic.CONTRACT.value, 'topic': 'Договорной отдел'},
]

order_topic_tuple = ((OrderTopic.TECH.value, 'Техническая проблема'), (OrderTopic.CONTRACT.value, 'Договорной отдел'))


# вкладки
class CountSelector(str, Enum):
    REQUEST = 'id_menu_request'
    NEWS = 'id_menu_news'
    PUSH = 'id_menu_push'
    CLIENT = 'id_client_chat'
    CURATOR = 'id_curator_chat'


# ПО
class Soft(str, Enum):
    B_SMART = 'b_smart'
    ADMIN_D = 'admin_d'
    S_SMART = 's_smart'
    P_SMART = 'p_smart'
    WEB_T = 'web_t'
    DIGIT_B = 'digit_b'
    O_SMART = 'o_smart'


soft_dict = {
    Soft.B_SMART.value: 'ПК "Бюджет-СМАРТ Про"',
    Soft.ADMIN_D.value: 'ПК "Администратор-Д"',
    Soft.S_SMART.value: 'ПК "Свод-СМАРТ"',
    Soft.P_SMART.value: 'ПРОЕКТИРОВАНИЕ БЮДЖЕТА: "Проект-СМАРТ Про"',
    Soft.WEB_T.value: 'ПК "WEB-Торги-КС"',
    Soft.DIGIT_B.value: 'ПК "Взаимодействие с порталом "Электронный бюджет" по приказу 243н"',
    Soft.O_SMART.value: 'ПК "Собственность-СМАРТ"',
}


soft_list_dict = [
    {'id': Soft.B_SMART.value, 'title': 'ПК "Бюджет-СМАРТ Про"'},
    {'id': Soft.ADMIN_D.value, 'title': 'ПК "Администратор-Д"'},
    {'id': Soft.S_SMART.value, 'title': 'ПК "Свод-СМАРТ"'},
    {'id': Soft.P_SMART.value, 'title': 'ПРОЕКТИРОВАНИЕ БЮДЖЕТА, "Проект-СМАРТ Про"'},
    {'id': Soft.WEB_T.value, 'title': 'ПК "WEB-Торги-КС"'},
    {'id': Soft.DIGIT_B.value, 'title': 'ПК "Взаимодействие с порталом "Электронный бюджет" по приказу 243н"'},
    {'id': Soft.O_SMART.value, 'title': 'ПК "Собственность-СМАРТ"'},
]

# soft_tuple = ((k, v) for k, v in soft_dict.items())
soft_tuple = (
    (Soft.B_SMART.value, 'ПК "Бюджет-СМАРТ Про"'),
    (Soft.ADMIN_D.value, 'ПК "Администратор-Д"'),
    (Soft.S_SMART.value, 'ПК "Свод-СМАРТ"'),
    (Soft.P_SMART.value, 'ПРОЕКТИРОВАНИЕ БЮДЖЕТА: "Проект-СМАРТ Про"'),
    (Soft.WEB_T.value, 'ПК "WEB-Торги-КС"'),
    (Soft.DIGIT_B.value, 'ПК "Взаимодействие с порталом "Электронный бюджет" по приказу 243н"'),
    (Soft.O_SMART.value, 'ПК "Собственность-СМАРТ"'),
)


# ПО
class CustomerType(str, Enum):
    MY = 'my'
    GY = 'gy'


customer_type_dict = {
    CustomerType.MY.value: 'МУ',
    CustomerType.GY.value: 'ГУ'
}

# customer_type_tuple = ((k, v) for k, v in customer_type_dict.items())
customer_type_tuple = ((CustomerType.MY.value, 'МУ'), (CustomerType.GY.value, 'ГУ'))
