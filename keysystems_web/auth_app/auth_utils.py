from django.http.request import HttpRequest

from .models import Password
from common.models import UserKS

from common import log_error, pass_gen, send_password_email


def send_password(user: UserKS, request: HttpRequest) -> int:
    password = pass_gen()
    new_pass = Password(password=password, user_ks=user)
    new_pass.save()
     # тут пароль отправляем на почту
    login_url = f'http://{request.get_host()}/index_2_2?pass={new_pass.pk}'
    login_url = f'http://{request.get_host()}/index_2_2?pass=5'

    send_password_email(user_email=user.username, password=password, login_url=login_url)
    # send_password_email(user_email='dgushch@gmail.com', password=password, login_url=login_url)

    return new_pass.id
    # return 5
