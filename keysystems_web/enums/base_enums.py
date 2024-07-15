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