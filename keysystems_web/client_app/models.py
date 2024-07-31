from django.db import models
from ckeditor.fields import RichTextField

from common.models import UserKS, Soft
from enums import OrderStatus


# Новости
class News(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    author = models.CharField('автор', max_length=255, null=True, blank=True)
    title = models.CharField('Название', max_length=255)
    text_preview = models.TextField('Текст привью', null=True, blank=True)
    text = RichTextField('Текст')
    photo = models.ImageField ('Фото', upload_to="news", null=True, blank=True)

    is_active = models.BooleanField(default=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'news'


# просмотренные новости
class ViewNews(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='view_news')
    user_ks = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='view_news')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Просмотр новости'
        verbose_name_plural = 'Просмотр новостей'
        db_table = 'view_news'


# # обновления ПО
class UpdateSoft(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    soft = models.ForeignKey(Soft, on_delete=models.DO_NOTHING, related_name='update_soft', verbose_name='Обновления ПО')
    description = RichTextField('Описание')
    is_active = models.BooleanField(default=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Обновления ПО'
        verbose_name_plural = 'Обновления ПО'
        db_table = 'soft_updates'


# файлы обновления ПО
class UpdateSoftFiles(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    update_soft = models.ForeignKey(UpdateSoft, on_delete=models.DO_NOTHING, related_name='files', verbose_name='Обновления ПО')
    file = models.FileField('Путь', upload_to='updates')
    file_size = models.PositiveIntegerField('Размер файла (в байтах)', null=True, blank=True)

    objects: models.Manager = models.Manager()

    def save(self, *args, **kwargs):
        if self.file and not self.file_size:
            self.file_size = self.file.size
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Обновления ПО'
        verbose_name_plural = 'Обновления ПО'
        db_table = 'su_files'


# просмотренные файлы обновления
class ViewUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    update_soft = models.ForeignKey(UpdateSoft, on_delete=models.CASCADE, related_name='view_update')
    user_ks = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='view_update')
    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Просмотр обновлений'
        verbose_name_plural = 'Просмотр обновлений'
        db_table = 'view_update'


# Частые вопросы
class FAQ(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлена', auto_now=True)
    question = models.TextField('Вопрос')
    answer = RichTextField('Ответ')
    is_active = models.BooleanField('Активно', default=True)

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        db_table = 'faq'


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


'''
{
    "model": "common.ordertopic",
    "pk": 1,
    "fields": {
        "topic": "Сломаль(",
        "is_active": true
    }
}
'''
