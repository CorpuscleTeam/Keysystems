# from django.urls import path
# from keysystems_web.consumers import ChatConsumer

# import os
# import logging
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'keysystems_web.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 [
#                     path('ws/chat/', ChatConsumer.as_asgi()),
#                 ]
#             )
#         )
#     ),
# })
#
# websocket_urlpatterns = [
    # path('ws/chat/', ChatConsumer.as_asgi()),
    # path('ws/', ChatConsumer.as_asgi()),
# ]
