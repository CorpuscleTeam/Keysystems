from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime

from enums import OrderStatus, ORDER_CHOICES, notices_tuple, CHAT_CHOICES, MsgType, MSG_TYPE_CHOICES


# список районов
class District(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Название', max_length=255)

    objects = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        db_table = 'districts'


# модель клиентов customer
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    inn = models.BigIntegerField('ИНН', null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='customer', verbose_name='Район')
    title = models.CharField('Название', max_length=255)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        db_table = 'customers'


# пользователи
class UserKS(AbstractUser):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='user', verbose_name='Клиент', null=True, blank=True)
    email = models.CharField('Почта', max_length=100, null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=255, default='Админ')
    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)

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
    user = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='used_soft')
    soft = models.ForeignKey(Soft, on_delete=models.CASCADE, related_name='used_soft')

    objects = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'ПО пользователей'
        verbose_name_plural = 'ПО пользователей'
        db_table = 'used_soft'


# темы обращений
class OrderTopic(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('Тема', max_length=255)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = 'Тема обращения'
        verbose_name_plural = 'Темы обращений'
        db_table = 'orders_topics'


# заказы
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    from_user = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='created_orders', verbose_name='Пользователь')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    text = models.CharField('Текст', max_length=255)
    soft = models.ForeignKey(Soft, on_delete=models.DO_NOTHING, related_name='order', verbose_name='ПО')
    topic = models.ForeignKey(OrderTopic, on_delete=models.DO_NOTHING, related_name='order', verbose_name='Тема')
    status = models.CharField('Статус', default=OrderStatus.NEW.value, choices=ORDER_CHOICES)

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
    user_ks = models.ForeignKey(UserKS, on_delete=models.DO_NOTHING, related_name='downloaded_file')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='downloaded_file')
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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='notice')
    user_ks = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='notice')
    text = models.CharField('Текст', max_length=255)
    viewed = models.BooleanField(default=False)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"Notice {self.text}"

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        db_table = 'notice'


# районы и по кураторов
class CuratorDist(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    user = models.ForeignKey(UserKS, on_delete=models.DO_NOTHING, related_name='curator_dist')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='curator_dist')
    soft = models.ForeignKey(Soft, on_delete=models.DO_NOTHING, related_name='curator_dist')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Распределение кураторов'
        verbose_name_plural = 'Распределения кураторов'
        db_table = 'curator_dist'


# кураторы заявки
class OrderCurator(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    user = models.ForeignKey(UserKS, on_delete=models.DO_NOTHING, related_name='order_curator')
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='order_curator')

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
    type_msg = models.CharField('Тип сообщения', max_length=255, default=MsgType.MSG.value, choices=MSG_TYPE_CHOICES)
    from_user = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='message')
    chat = models.CharField('Чат', choices=CHAT_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='message')
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
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='view_message')
    user_ks = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='view_message')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Просмотр сообщения'
        verbose_name_plural = 'Просмотр сообщений'
        db_table = 'view_message'
