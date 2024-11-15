from django.urls import path

from client_app import views as client
from auth_app.views import start_page_redirect


urlpatterns = [
    path('', start_page_redirect, name='redirect'),
    path('news/', client.index_4_1, name='index_4_1'),  # /client/news
    path('news/<int:news_id>/', client.index_4_2, name='index_4_2'),  # /client/news/<номер публикации>
    path('dashboard/', client.index_5_1, name='index_5_1'),  # /client/dashboard
    path('notifications/', client.index_6, name='index_6'),  # /client/notifications
    path('upgrade/', client.index_7_1, name='index_7_1'),  # /client/upgrade
    path('upgrade/<int:update_id>/', client.index_7_2, name='index_7_2'),  # /client/upgrade/<номер публикации>
    path('question/', client.index_8, name='index_8'),  # /client/question
]