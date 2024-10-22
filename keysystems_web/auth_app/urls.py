from django.urls import path

from auth_app import views as reg


urlpatterns = [
    path('', reg.index_2, name='index_2'),  # /auth/
    path('login/', reg.index_2_1, name='index_2_1'),  # /auth/login
    path('password/', reg.index_2_2, name='index_2_2'),  # /auth/password
    path('register/', reg.index_3_1, name='index_3_1'),  # /auth/register
    # path('register-success/', reg.index_3_2, name='index_3_2'),  # /auth/register-success
]
