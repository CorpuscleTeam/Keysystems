from django.http import JsonResponse
from .models import Order
from .serializers import OrderSerializer, DownloadedFileSerializer

import logging


def get_order_data(request, order_id):
    # logging.warning(f'>>>>>>>> order_id:{order_id}')
    try:
        order = Order.objects.filter(id=14).first()
        messages =

        return JsonResponse(
            {
                'order': OrderSerializer(order),

        }, safe=False)
    except Exception as ex:
        logging.warning(ex)
        return JsonResponse({'error': 'not found'}, status=404)
