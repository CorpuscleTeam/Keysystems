from django.http import JsonResponse
from .models import Order
from .serializers import OrderSerializer

import logging


def get_order_data(request, order_id):
    logging.warning(f'>>>>>>>> order_id:{order_id}')
    try:
        order = Order.objects.filter(id=5).first()
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data, safe=False)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
