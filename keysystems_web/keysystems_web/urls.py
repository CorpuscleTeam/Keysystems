from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
from auth_app import views as reg
from client_app import views as client
from curator_app import views as curator
from common import views as com


urlpatterns = [
    path('', reg.start_page_redirect, name='redirect'),
    path('logout', reg.logout_view, name='logout'),

    path("edit-order", com.edit_order_view),
    path("tab-action", com.viewed_msg_view),
    path("get-curators", com.get_curator_view),
    path("order-soft", com.edit_order_soft_view),

    path("test", com.test),

    path('index_2', reg.index_2, name='index_2'),
    path('index_2_1', reg.index_2_1, name='index_2_1'),
    path('index_2_2', reg.index_2_2, name='index_2_2'),
    path('index_3_1', reg.index_3_1, name='index_3_1'),
    path('index_4_1', client.index_4_1, name='index_4_1'),
    path('index_4_2', client.index_4_2, name='index_4_2'),

    path('index_8', client.index_8, name='index_8'),
    path('index_5_1', client.index_5_1, name='index_5_1'),
    path('index_6', client.index_6, name='index_6'),
    path('index_7_1', client.index_7_1, name='index_7_1'),
    path('index_7_2', client.index_7_2, name='index_7_2'),

    path('cur_index_1_1', curator.cur_index_1_1, name='cur_index_1_1'),
    path('cur_index_2_1', curator.cur_index_2_1, name='cur_index_2_1'),
    path('cur_index_3', curator.cur_index_3, name='cur_index_3'),

    path('admin/', admin.site.urls),

    path('order-data/<int:order_id>/', com.get_order_data, name='order_data'),
    path("ckeditor5/", include('django_ckeditor_5.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

