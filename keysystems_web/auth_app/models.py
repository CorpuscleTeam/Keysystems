from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password, check_password

from common.models import UserKS


# просмотренные сообщений
class Password(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    password = models.CharField('Пароль', max_length=20)
    user_ks = models.ForeignKey(UserKS, on_delete=models.CASCADE, related_name='password_ot')

    objects: models.Manager = models.Manager()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'Пароль'
        verbose_name_plural = 'Пароли'
        db_table = 'passwords'
