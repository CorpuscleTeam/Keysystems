from django.contrib import admin
from django.urls import path

from auth_app import views as reg
from client_app import views as client

urlpatterns = [
    path('', reg.start_page_redirect, name='redirect'),
    path('index_2', reg.index_2, name='index_2'),
    path('index_2_1', reg.index_2_1, name='index_2_1'),
    path('index_2_2', reg.index_2_2, name='index_2_2'),
    path('index_3_1', reg.index_3_1, name='index_3_1'),
    path('index_3_2', client.index_3_2, name='index_3_2'),
    path('index_4_1', client.index_4_1, name='index_4_1'),
    path('index_4_2', client.index_4_2, name='index_4_2'),
    path('admin/', admin.site.urls),
]
