from django.db import models

from datetime import datetime

from enums import ENTRY_TYPES, OrderStatus


# модель клиентов customer
class News(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    type_entry = models.CharField('Тип', max_length=50, choices=ENTRY_TYPES)
    author = models.CharField('автор', max_length=255, null=True, blank=True)
    title = models.CharField('Название', max_length=255)
    text_preview = models.TextField('Текст привью', null=True, blank=True)
    text = models.TextField('Текст')
    photo = models.CharField('Фото', max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'news'


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