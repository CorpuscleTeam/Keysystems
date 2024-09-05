from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.serializers import serialize

import logging

from keysystems_web.settings import DEBUG
from .forms import AuthBaseForm, RegistrationForm, PasswordForm, AuthUserForm
from .models import Password
from common.models import UserKS, Soft, Customer, District, UsedSoft
from common.logs import log_error
from common import log_error, pass_gen, send_password_email, get_current_url
from enums import RequestMethod


# Определяет начальную страницу пользователя
def start_page_redirect(request: HttpRequest):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('cur_index_1_1')

    elif request.user.is_authenticated:
        return redirect('index_4_1')

    else:
        return redirect('index_2')


# выход
def logout_view(request):
    logout(request)
    return redirect('redirect')


# первая клиентская страница. Просит инн
def index_2(request: HttpRequest):
    if request.user.is_authenticated and not DEBUG:
        return redirect('redirect')

    error_msg = {'text_error': '', 'type_error': ''}
    if request.method == RequestMethod.POST:
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            input_inn = form.cleaned_data["inn"]
            costumer = Customer.objects.filter(inn=input_inn).first()
            users_inn = UserKS.objects.filter(customer=costumer).all()
            log_error(f'>>len(users_inn): {len(users_inn)}', wt=False)

            if len(users_inn) == 0:
                if costumer:
                    return redirect(reverse('index_3_1') + f'?inn={input_inn}')
                else:
                    error_msg = {'text_error': 'ИНН не зарегистрирован', 'type_error': 'inn'}

            elif len(users_inn) == 1:
                password = pass_gen()
                new_pass = Password(password=password, user_ks=users_inn[0])
                new_pass.save()
                #  тут пароль отправляем на почту
                login_url = f'http://{request.get_host()}/index_2_2?pass={new_pass.pk}'

                send_password_email(user_email=users_inn[0].username, password=password, login_url=login_url)

                return redirect(reverse('index_2_2') + f'?pass={new_pass.id}')

            elif len(users_inn) > 1:
                return redirect(reverse('index_2_1') + f'?inn={input_inn}')

            else:
                return redirect('index_2_2')
        else:
            error_msg = {'text_error': 'Некорректный ИНН', 'type_error': 'inn'}

    context = {**error_msg}
    return render(request, 'auth/index_2.html', context)


#
def index_2_1(request: HttpRequest):
    if request.user.is_authenticated and not DEBUG:
        return redirect('redirect')

    error_msg = {'text_error': '', 'type_error': ''}
    input_inn = request.GET.get('inn', '')
    input_email = request.POST.get('email')
    if request.method == RequestMethod.POST:
        auth_form = AuthUserForm(request.POST)
        if auth_form.is_valid():
            customer = Customer.objects.get(inn=auth_form.cleaned_data['inn'])
            user = UserKS.objects.filter(
                customer=customer,
                username=auth_form.cleaned_data['email']
            ).first()
            if user:
                password = pass_gen()
                new_pass = Password(password=password, user_ks=user)
                new_pass.save()
                #  тут пароль отправляем на почту
                login_url = f'http://{request.get_host()}/index_2_2?pass={new_pass.id}'

                send_password_email(user_email=user.username, password=password, login_url=login_url)
                return redirect(reverse('index_2_2') + f'?pass={new_pass.pk}')

            else:
                return redirect('index_3_1')

        else:
            error_data = auth_form.errors.as_data()
            if error_data.get('inn'):
                error_msg = {'text_error': 'Неправильный формат ИНН', 'type_error': 'inn'}
            elif error_data.get('email'):
                error_msg = {'text_error': 'Некорректный email', 'type_error': 'email'}
            else:
                error_msg = {'text_error': 'Ошибка ввода', 'type_error': 'inn'}

    context = {**error_msg, 'inn': input_inn, 'email': input_email}
    return render(request, 'auth/index_2_1.html', context)


# принимает пароль и регистрирует пользователя
# Bz315sk3 | id 7
def index_2_2(request: HttpRequest):
    if request.user.is_authenticated and not DEBUG:
        return redirect('redirect')

    error_msg = {'text_error': '', 'type_error': ''}
    pass_id = request.GET.get('pass', 0)

    if request.method == RequestMethod.POST:
        pass_form = PasswordForm(request.POST)
        if pass_form.is_valid():
            # user_id = request.POST.get('pass', 0)
            # user = UserKS.objects.filter(id=user_id).first()
            log_error(f'{pass_form.cleaned_data["password"]} {int(pass_id)}', wt=False)
            user_info = Password.objects.select_related('user_ks').filter(
                password=pass_form.cleaned_data['password'],
                id=int(pass_id)
            ).first()

            if user_info:
                login(request, user_info.user_ks)
                if not pass_form.cleaned_data['checkbox']:
                    request.session.set_expiry(0)

                user_info.delete()  # удаляем использованный пароль
                return redirect('redirect')

            else:
                error_msg = {'text_error': 'Неверный пароль', 'type_error': 'password'}
        else:
            error_msg = {'text_error': 'Пароль не найден', 'type_error': 'password'}

    context = {
        **error_msg,
        'pass_id': pass_id
    }
    return render(request, 'auth/index_2_2.html', context)


# регистрация заполните форму
def index_3_1(request: HttpRequest):
    if request.user.is_authenticated and not DEBUG:
        return redirect('redirect')

    error_msg = {'text_error': '', 'type_error': ''}

    if request.method == RequestMethod.POST:
        # log_error(request.POST, wt=False)
        reg_form = RegistrationForm(request.POST)
        inn = Customer.objects.filter(inn=reg_form.data.get('inn', 0))
        if reg_form.is_valid() and inn:
            email = reg_form.cleaned_data['email']
            email = email[len('mailto:'):] if email.startswith('mailto:') else email
            user = UserKS.objects.filter(username=email).first()
            if user:
                error_msg = f'Почта {email} уже зарегистрирована'

            else:
                new_user = UserKS(
                    username=email,
                    customer=Customer.objects.get(inn=reg_form.cleaned_data['inn']),
                    full_name=reg_form.cleaned_data['fio'],
                    phone=reg_form.cleaned_data['tel']
                )
                new_user.save()

                #  тут пароль отправляем на почту
                password = pass_gen()
                new_pass = Password(password=password, user_ks=new_user)
                new_pass.save()
                login_url = f'http://{request.get_host()}/index_2_2?pass={new_pass.pk}'
                send_password_email(user_email=email, password=password, login_url=login_url)
                # send_pass_email(email=email, password=password)

                used_soft = Soft.objects.get(id=reg_form.cleaned_data['reg_progr'])
                UsedSoft.objects.create(user=new_user, soft=used_soft)
                return redirect(reverse('index_2_2') + f'?pass={new_pass.pk}')
                # return redirect(reverse('index_2_2') + f'?user={new_user.pk}')

        else:
            error_data = reg_form.errors.as_data()
            if error_data.get('inn'):
                error_msg = {'text_error': 'Неправильный формат ИНН', 'type_error': 'inn'}
            elif error_data.get('email'):
                error_msg = {'text_error': 'Некорректный email', 'type_error': 'email'}
            elif error_data.get('fio'):
                error_msg = {'text_error': 'Имя не может быть пустым', 'type_error': 'fio'}
            elif error_data.get('tel'):
                error_msg = {'text_error': 'Телефон не может быть пустым', 'type_error': 'tel'}
            else:
                error_msg = {'text_error': 'Ошибка ввода', 'type_error': 'inn'}

    input_inn = request.POST.get('inn', '') if request.POST.get('inn', '') else request.GET.get('inn', '')
    context = {
        **error_msg,
        'soft': serialize(format='json', queryset=Soft.objects.filter(is_active=True).all()),
        'inn': input_inn,
        'email': request.POST.get('email', ''),
        'fio': request.POST.get('fio', ''),
        'tel': request.POST.get('tel', ''),
    }
    return render(request, 'auth/index_3_1.html', context)
