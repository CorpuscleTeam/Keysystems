from urllib.parse import urlparse

import os
import logging

from rest_framework import serializers
from .models import News, UpdateSoft, UpdateSoftFiles
import common as ut
from common.logs import log_error
from enums import notices_dict, soft_dict, order_topic_dict


'''
/*{
    "model": "client_app.news",
    "pk": 1,
    "fields": {
        "created_at": "2024-07-23T08:05:33.090Z",
        "updated_at": "2024-07-23T08:05:33.090Z",
        "type_entry": "news",
        "author": "Иванов Иван",
        "title": "Новейшество",
        "text_preview": "15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як",
        "text": "15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як\r\n15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як\r\n15.05.2024 с 08.00 по 10.00 ведутся внеплановые технические работы на сервере ПО «Бюджет-СМАРТ» (республиканская база).\r\nДоступ в программу будет восстановлен после 10.00 як",
        "photo": "news/5c23a3e243fb3167eb382be6.png",
        "is_active": true,
        "day": 23,
        "month": "Июля",
        "year": 2024
    }
} */
'''


# уведомления
class NewsSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'day', 'month', 'year', 'title', 'author', 'text_preview', 'text', 'photo']

    def get_day(self, obj):
        return obj.created_at.day

    def get_month(self, obj):
        return ut.months_str_ru.get(obj.created_at.month, '')

    def get_year(self, obj):
        return obj.created_at.year

    def get_photo(self, obj):
        log_error(f'>>> {obj.photo} {obj.photo}', wt=False)
        if not obj.photo:
            log_error(f'>>> {obj.photo} {obj.photo}', wt=False)
        return obj.photo.url if obj.photo else None


class UpdateFilesSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = UpdateSoftFiles
        fields = ['url', 'name', 'icon']

    def get_url(self, obj):
        return f'{obj.file.url}' if obj.file else None

    def get_name(self, obj):
        return obj.file.name.split('/')[-1]

    def get_icon(self, obj):
        return ut.get_file_icon_link(obj.file.url)


class UpdateSoftSerializer(serializers.ModelSerializer):
    # updates = UpdateFilesSerializer()
    update_files = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    soft = serializers.SerializerMethodField()

    class Meta:
        model = UpdateSoft
        fields = ['date', 'soft', 'description', 'update_files']
        # fields = ['id', 'date', 'soft', 'description']

    def get_date(self, obj):
        return ut.get_date_string(obj.created_at)

    def get_soft(self, obj):
        return soft_dict.get(obj.soft, '')

    def get_update_files(self, obj):
        files = UpdateSoftFiles.objects.filter(update_soft=obj).all()
        return UpdateFilesSerializer(files, many=True).data

'''
  "date": "ВЧЕРА / 15:25",
     "soft": "ПО 3",
     "description": "Программный комплекс «WEB-Торги-КС» предоставляет возможности автоматизированной работы для следующих групп пользователей",
     "update_files": [
         {
             "url": "/media/updates/5c23a3e243fb3167eb382be6.png",
             "name": "updates/5c23a3e243fb3167eb382be6.png"
         },
         {
             "url": "/media/updates/H8fJYUqYp9.jpeg",
             "name": "updates/H8fJYUqYp9.jpeg"
         }
     ]
'''