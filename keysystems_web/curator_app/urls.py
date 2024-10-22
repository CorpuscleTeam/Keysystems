from django.urls import path

from curator_app import views as curator
from auth_app.views import start_page_redirect


urlpatterns = [
    path('', start_page_redirect, name='redirect'),
    path('mydashboard/', curator.cur_index_1_1, name='cur_index_1_1'),  # /curator/mydashboard
    path('alldashboard/', curator.cur_index_2_1, name='cur_index_2_1'),  # /curator/alldashboard
    path('notifications/', curator.cur_index_3, name='cur_index_3'),  # /curator/notifications
]
