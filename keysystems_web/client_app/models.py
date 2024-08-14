from django.db import models
# from ckeditor.fields import RichTextField
from django.db.models.fields import TextField as RichTextField

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
