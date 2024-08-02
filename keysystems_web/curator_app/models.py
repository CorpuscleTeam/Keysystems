from django.db import models
from datetime import datetime

from common.models import District, UserKS, Soft, Order
from enums import OrderStatus, ORDER_CHOICES, notices_tuple


# районы и по кураторов
# class CuratorDist(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField('Создана', auto_now_add=True)
#     updated_at = models.DateTimeField('Обновлена', auto_now=True)
#     user = models.ForeignKey(UserKS, on_delete=models.DO_NOTHING, related_name='curator_dist')
#     district = models.ForeignKey(District, on_delete=models.DO_NOTHING, related_name='curator_dist')
#     soft = models.ForeignKey(Soft, on_delete=models.DO_NOTHING, related_name='curator_dist')
#
#     objects: models.Manager = models.Manager()
#
#     def __str__(self):
#         return f"{self.user}"
#
#     class Meta:
#         verbose_name = 'Распределение кураторов'
#         verbose_name_plural = 'Распределения кураторов'
#         db_table = 'curator_dist'
#
#
# # кураторы заявки
# class OrderCurator(models.Model):
#     id = models.AutoField(primary_key=True)
#     created_at = models.DateTimeField('Создана', auto_now_add=True)
#     updated_at = models.DateTimeField('Обновлена', auto_now=True)
#     user = models.ForeignKey(UserKS, on_delete=models.DO_NOTHING, related_name='curator_dist')
#     order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, related_name='curator_dist')
#
#     objects: models.Manager = models.Manager()
#
#     def __str__(self):
#         return f"{self.user}"
#
#     class Meta:
#         verbose_name = 'Распределение кураторов'
#         verbose_name_plural = 'Распределения кураторов'
#         db_table = 'curator_dist'
