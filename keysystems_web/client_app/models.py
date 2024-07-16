from django.db import models
from auth_app.models import CustomUser

from datetime import datetime

from enums import ORDER_CHOICES, OrderStatus


# темы обращений
class OrderTopic(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Тема обращения'
        verbose_name_plural = 'Темы обращений'
        db_table = 'orders_topics'


# Список ПО
class Soft(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'ПО'
        verbose_name_plural = 'ПО'
        db_table = 'soft'


# используемое ПО
class UsedSoft(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='used_soft')
    soft = models.ForeignKey(Soft, on_delete=models.CASCADE, related_name='used_soft')

    objects = models.Manager()

    class Meta:
        verbose_name = 'ПО пользователей'
        verbose_name_plural = 'ПО пользователей'
        db_table = 'used_soft'


# заказы
# class Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField('Создана', default=datetime.now())
#     updated_at = models.DateTimeField('Обновлена', default=datetime.now())
#     from_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='order')
#     text = models.CharField('Текст', max_length=255)
#     soft = models.ForeignKey(Soft, on_delete=models.DO_NOTHING, related_name='order')
#     executor = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='order')
#     status = models.CharField('Статус', default=OrderStatus.NEW.value, choices=ORDER_CHOICES)

#     objects = models.Manager()

#     class Meta:
#         verbose_name = 'Заявка'
#         verbose_name_plural = 'Заявки'
#         db_table = 'orders'


# новости. хз как оно будет работать
def news():
    return [
        {'id': 1,
         'title': 'Ускорение',
         'text': 'В последнее время пользователи Кейсистем заметили значительное увеличение скорости соединения. '
                 'Это стало возможным благодаря обновлению инфраструктуры и оптимизации сетевых маршрутов. '
                 'Теперь пользователи могут воспользоваться более быстрой и надежной связью, что особенно важно для '
                 'работы и учебы удаленно.',
         'day': '1',
         'month': 'Июля',
         'year': '2024',
         'author': 'Иван Иванов',
         'photo': '/media/news/example.jpg',
         },
        {
         'id': 2,
         'title': 'Расширение',
         'text': 'Кейсистем представил новые услуги для своих клиентов. Среди них – бесплатный Wi-Fi в общественных '
                 'местах, расширенный пакет данных для мобильных устройств и скидки на абонентскую плату для новых '
                 'подписчиков. Эти изменения направлены на улучшение качества жизни пользователей и '
                 'привлечение новых клиентов.',
         'day': '15',
         'month': 'Июля',
         'year': '2024',
         'author': 'Петр Петров',
         'photo': '/media/news/example.jpg',
         },
        {'id': 3,
         'title': 'Модернизация',
         'text': 'Текст: Для обеспечения стабильности и надежности связи Кейсистем проводит масштабное обновление '
                 'своего оборудования. Более 50% базовых станций уже были модернизированы, а остальные будут '
                 'обновлены к концу года. Это позволит улучшить покрытие и качество сигнала в регионе.',
         'day': '20',
         'month': 'Июля',
         'year': '2024',
         'author': 'Сергей Сергеев',
         'photo': '/media/news/example.jpg',
         },
        {'id': 4,
         'title': 'Экологическая инициатива',
         'text': 'Текст: Кейсистем запустил экологическую программу, направленную на снижение влияния своей '
                 'деятельности на окружающую среду. В рамках этой инициативы компания планирует установить солнечные '
                 'панели на крышах своих объектов и использовать возобновляемую энергию для питания серверов. '
                 'Это не только поможет сэкономить ресурсы, но и сделает работу компании более устойчивой к '
                 'изменяющимся условиям климата.',
         'day': '30',
         'month': 'Июля',
         'year': '2024',
         'author': 'Мария Марина',
         'photo': '/media/news/example.jpg',
         },
    ]