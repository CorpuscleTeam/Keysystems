import json

from rest_framework import serializers
from .models import Order, Soft, OrderTopic, UserKS, OrderCurator, Customer
from common import get_data_string
from .logs import log_error
from enums import notices_dict


class SoftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soft
        fields = ['id', 'title', 'description', 'is_active']


class OrderTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTopic
        fields = ['id', 'topic', 'is_active']


class UserKSSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserKS
        fields = ['id', 'full_name', 'username']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'inn', 'district', 'title']


class OrderCuratorSerializer(serializers.ModelSerializer):
    user = UserKSSerializer()

    class Meta:
        model = OrderCurator
        fields = ['id', 'user']


class OrderSerializer(serializers.ModelSerializer):
    soft = SoftSerializer()
    topic = OrderTopicSerializer()
    from_user = UserKSSerializer()
    customer = CustomerSerializer()
    order_curators = OrderCuratorSerializer(many=True, source='order_curator')

    id_str = serializers.SerializerMethodField()
    curators = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'from_user', 'customer', 'text', 'soft', 'topic', 'status', 'id_str', 'order_curators', 'curators']

    def get_id_str(self, obj):
        return f'#{str(obj.id).zfill(5)}'

    def get_curators(self, obj):
        curators = [curator.user.full_name for curator in obj.order_curator.all()]
        if curators:
            return ', '.join(curators)
        else:
            return 'Нет куратора'


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
                        'date': get_data_string(notice.created_at),
                        'text': text.format(pk=notice.id)
                    }
                )
        return json.dumps(self.notice_list)
