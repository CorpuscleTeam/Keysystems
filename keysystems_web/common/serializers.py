from urllib.parse import urlparse

import os
import json
import logging

from rest_framework import serializers
from .models import Order, Soft, OrderTopic, UserKS, OrderCurator, Customer, District, DownloadedFile
from common import get_date_string, get_size_file_str, get_file_icon_link
from .logs import log_error
from enums import notices_dict


# районы
class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['title']


# районы
class DownloadedFileSerializer(serializers.ModelSerializer):
    filename = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    file_size = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = DownloadedFile
        # fields = ['url']
        fields = ['url', 'filename', 'file_size', 'icon']

    def get_filename(self, obj):
        parsed_url = urlparse(obj.url)
        return os.path.basename(parsed_url.path)

    def get_url(self, obj):
        return f'..{obj.url}'

    def get_file_size(self, obj):
        if obj.file_size:
            return get_size_file_str(obj.file_size)
        else:
            return 'н/д'

    def get_icon(self, obj):
        return get_file_icon_link(obj.url)


# ПО
class SoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soft
        fields = ['id', 'title', 'description', 'is_active']


# Обращения
class OrderTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTopic
        fields = ['id', 'topic', 'is_active']


# пользователи
class UserKSSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKS
        fields = ['id', 'full_name', 'username']


# районыклиент
class CustomerSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = Customer
        fields = ['id', 'inn', 'district', 'title']


# кураторы
class OrderCuratorSerializer(serializers.ModelSerializer):
    user = UserKSSerializer()

    class Meta:
        model = OrderCurator
        fields = ['id', 'user']


# заказы полные данные
class OrderSerializer(serializers.ModelSerializer):
    soft = SoftSerializer()
    topic = OrderTopicSerializer()
    from_user = UserKSSerializer()
    customer = CustomerSerializer()
    files = DownloadedFileSerializer(many=True, source='downloaded_file')
    order_curators = OrderCuratorSerializer(many=True, source='order_curator')

    id_str = serializers.SerializerMethodField()
    curators = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'from_user', 'customer', 'text', 'soft', 'topic', 'status', 'id_str', 'order_curators', 'curators', 'files'
        ]

    def get_id_str(self, obj):
        return f'#{str(obj.id).zfill(5)}'

    def get_curators(self, obj):
        curators = [curator.user.full_name for curator in obj.order_curator.all()]
        if curators:
            return ', '.join(curators)
        else:
            return 'Нет куратора'


# уведомления
class NoticeSerializer:
    def __init__(self, notices: list):
        self.notices = notices
        self.notice_list = []

    def serialize(self) -> str:
        for notice in self.notices:
            text: str = notices_dict.get(notice.type_notice)
            if text:
                self.notice_list.append(
                    {
                        'order_id': notice.order.id,
                        'num_push': notice.id,
                        'date': get_date_string(notice.created_at),
                        'text': text.format(pk=notice.id)
                    }
                )
        return json.dumps(self.notice_list)
