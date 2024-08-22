from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.hashers import make_password, check_password



# class UserKS(models.Model):
#     ROLE_CHOICES = (
#         (UserRole.CLIENT.value, 'Клиент'),
#         (UserRole.STAFF.value, 'Staff'),
#     )
#     id = models.AutoField(primary_key=True)
#     inn = models.BigIntegerField('ИНН')
#     email = models.CharField('Почта', max_length=100, null=True, blank=True)
#     full_name = models.CharField('ФИО', max_length=255, null=True, blank=True)
#     phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
#     password = models.CharField('Пароль', max_length=100, null=True, blank=True)
#     role = models.CharField('Роль', max_length=10, choices=ROLE_CHOICES, default='client')
#     product_id = models.IntegerField('ПО ID')
#
#     objects = models.Manager()
#
#     def save(self, *args, **kwargs):
#         if self.password and not self.password.startswith('pbkdf2_'):
#             self.password = make_password(self.password)
#         super(UserKS, self).save(*args, **kwargs)
#
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)
#
#     def __str__(self):
#         return f"<User({self.inn} {self.email})>"
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         db_table = 'users_ks'
