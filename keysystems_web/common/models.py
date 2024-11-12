from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime

from .logs import log_error
import enums as e


# министерства
class Ministry(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    name = models.TextField('Название')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Министерство'
        verbose_name_plural = 'Министерства'
        db_table = 'ministries'


# модель клиентов customer
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    form_type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    inn = models.BigIntegerField('ИНН', null=True, blank=True)
    title = models.TextField('Название')
    short_name = models.CharField('Короткое название', max_length=255, null=True, blank=True)
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='customer')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['title']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        db_table = 'customers'


# пользователи
class UserKS(AbstractUser):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        related_name='user',
        verbose_name='Компания',
        null=True,
        blank=True
    )
    username = models.CharField('Почта', max_length=150, unique=True)
    # email = models.CharField('Почта', max_length=100, null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=255, default='Админ')
    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    inn = models.CharField('ИНН', max_length=12, null=True, blank=True)
    # is_staff = models.BooleanField('Статус куратора', default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # db_table = 'users_ks'


# Список ПО
class Soft(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название ПО', max_length=255)
    description = models.CharField('Описание', max_length=255)
    is_active = models.BooleanField('Активно', default=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = 'ПО'
        db_table = 'soft'


# используемое ПО (связывает пользователя и ПО)
class UsedSoft(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserKS, on_delete=models.SET_NULL, related_name='used_soft', null=True)
    soft = models.CharField('ПО', max_length=255, choices=e.soft_tuple, default=e.Soft.B_SMART.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'ПО пользователей'
        verbose_name_plural = 'ПО пользователей'
        db_table = 'used_soft'


# заказы
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    from_user = models.ForeignKey(UserKS, on_delete=models.SET_NULL, related_name='created_orders', verbose_name='Пользователь', null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='orders', verbose_name='Клиент', null=True)
    text = models.CharField('Текст', max_length=255)
    soft = models.CharField('ПО', max_length=255, choices=e.soft_tuple, default=e.Soft.B_SMART.value)
    topic = models.CharField('Тема', max_length=255, choices=e.order_topic_tuple, default=e.OrderTopic.TECH.value)
    status = models.CharField('Статус', default=e.OrderStatus.NEW.value, choices=e.ORDER_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return f"Order {self.id}"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        db_table = 'orders'


# загруженные файлы
class DownloadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', default=datetime.now())
    user_ks = models.ForeignKey(UserKS, on_delete=models.SET_NULL, null=True, related_name='downloaded_file')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='downloaded_file', null=True)
    url = models.CharField('Ссылка', max_length=255)
    file_size = models.PositiveIntegerField('Размер файла (в байтах)', null=True, blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Скаченный файл'
        verbose_name_plural = 'Скаченные файлы'
        db_table = 'downloaded_file'


# Уведомления
class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='notice', null=True)
    user_ks = models.ForeignKey(UserKS, on_delete=models.SET_NULL, related_name='notice', null=True)
    text = models.CharField('Текст', max_length=255)
    viewed = models.BooleanField(default=False)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"Notice {self.text}"

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        db_table = 'notice'


# кураторы заявки
class OrderCurator(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    user = models.ForeignKey(UserKS, on_delete=models.SET_NULL, null=True, related_name='order_curator')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='order_curator')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Распределение кураторов'
        verbose_name_plural = 'Распределения кураторов'
        db_table = 'order_curator'


# сообщения чатов
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    type_msg = models.CharField('Тип сообщения', max_length=255, default=e.MsgType.MSG.value, choices=e.MSG_TYPE_CHOICES)
    from_user = models.ForeignKey(UserKS, on_delete=models.SET_NULL, related_name='message', null=True)
    chat = models.CharField('Чат', choices=e.CHAT_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='message', null=True)
    text = models.TextField('Текст', null=True, blank=True)
    file_path = models.CharField('Путь', null=True, blank=True)
    file_size = models.PositiveIntegerField('Размер файла (в байтах)', null=True, blank=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"Message {self.id}"

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        db_table = 'messages'


# просмотренные сообщений
class ViewMessage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, related_name='view_message', null=True)
    user_ks = models.ForeignKey(UserKS, on_delete=models.SET_NULL, related_name='view_message', null=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Просмотр сообщения'
        verbose_name_plural = 'Просмотр сообщений'
        db_table = 'view_message'


# Распределение курьеров B_SMART
class SoftBSmart(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.B_SMART.value,
        verbose_name=e.soft_dict[e.Soft.B_SMART.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.B_SMART.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.B_SMART.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.B_SMART.value]}'
        db_table = 'soft_b_smart'


# Распределение курьеров ADMIN_D
class SoftAdminD(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        max_length=255,
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.ADMIN_D.value,
        verbose_name=e.soft_dict[e.Soft.ADMIN_D.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.ADMIN_D.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.ADMIN_D.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.ADMIN_D.value]}'
        db_table = 'soft_admin_d'


# Распределение курьеров S_SMART
class SoftSSmart(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.S_SMART.value,
        verbose_name=e.soft_dict[e.Soft.S_SMART.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.S_SMART.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.S_SMART.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.S_SMART.value]}'
        db_table = 'soft_s_smart'


# Распределение курьеров P_SMART
class SoftPSmart(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.P_SMART.value,
        verbose_name=e.soft_dict[e.Soft.P_SMART.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.P_SMART.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.P_SMART.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.P_SMART.value]}'
        db_table = 'soft_p_smart'


# Распределение курьеров WEB_T
class SoftWebT(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.WEB_T.value,
        verbose_name=e.soft_dict[e.Soft.WEB_T.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.WEB_T.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.WEB_T.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.WEB_T.value]}'
        db_table = 'soft_web_t'


# Распределение курьеров DIGIT_B
class SoftDigitB(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.DIGIT_B.value,
        verbose_name=e.soft_dict[e.Soft.DIGIT_B.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.DIGIT_B.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.DIGIT_B.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.DIGIT_B.value]}'
        db_table = 'soft_digit_b'


# Распределение курьеров O_SMART
class SoftOSmart(models.Model):
    id = models.AutoField(primary_key=True)
    prefix = models.CharField('Префикс', max_length=4, null=True, blank=True)
    type = models.CharField(
        'Тип',
        choices=e.customer_type_tuple,
        default=e.customer_type_dict[e.CustomerType.MY.value]
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name=e.Soft.O_SMART.value,
        verbose_name=e.soft_dict[e.Soft.O_SMART.value])
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name=e.Soft.O_SMART.value)

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Распределение {e.soft_dict[e.Soft.O_SMART.value]}'
        verbose_name_plural = f'Распределение {e.soft_dict[e.Soft.O_SMART.value]}'
        db_table = 'soft_o_smart'


# Распределение курьеров O_SMART
class SoftExceptions(models.Model):
    id = models.AutoField(primary_key=True)
   
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL, null=True,
        related_name='soft_exceptions',
        verbose_name='Исключения распределения'
    )
    user = models.ForeignKey(
        UserKS,
        on_delete=models.SET_NULL, null=True,
        related_name='soft_exceptions',
        verbose_name='Исключения распределения'
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = f'Исключение распределения'
        verbose_name_plural = f'Исключения распределения'
        db_table = 'soft_exceptions'
        