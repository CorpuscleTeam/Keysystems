import json

from rest_framework import serializers
from .models import Order, Soft, OrderTopic, UserKS, Customer
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


class OrderSerializer(serializers.ModelSerializer):
    soft = SoftSerializer()
    topic = OrderTopicSerializer()
    from_user = UserKSSerializer()
    executor = UserKSSerializer()
    customer = CustomerSerializer()

    id_str = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'from_user', 'customer', 'text', 'soft', 'topic', 'executor', 'status', 'id_str']

    def get_id_str(self, obj):
        return f'#{str(obj.id).zfill(5)}'


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
