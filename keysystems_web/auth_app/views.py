from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail

from .forms import AuthBaseForm, RegistrationForm, PasswordForm, AuthUserForm
from .models import UserKS, CustomUser
from base_utils import log_error, pass_gen
from enums import RequestMethod, UserRole


# Определяет начальную страницу пользователя
def start_page_redirect(request: HttpRequest):
    # send_mail(
    #     'Тестовое письмо',
    #     'Это тестовое письмо, отправленное через Postfix SMTP сервер.',
    #     'your_email@example.com',
    #     ['dgushch@gmail.com'],
    #     fail_silently=False,
    # )

    if request.user.is_authenticated and request.user.is_staff:
        return redirect('index_4_1')

    elif request.user.is_authenticated:
        return redirect('index_4_1')

    else:
        return redirect('index_2')


# выход
def logout_view(request):
    logout(request)
    return redirect('index_2')


# первая клиентская страница. Просит инн
def index_2(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    input_error = 0
    if request.method == RequestMethod.POST:
        # log_error(request.POST, wt=False)
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            # log_error(form.cleaned_data, wt=False)
            # log_error(form.data, wt=False)
            user_inn = form.cleaned_data["inn"]
            users_inn = UserKS.objects.filter(inn=user_inn).all()

            if len(users_inn) == 0:
                return redirect('index_3_1')

            elif len(users_inn) > 1:
                return redirect(reverse('index_2_1') + f'?inn={users_inn}')

            else:
                return redirect('index_2_2')
        else:
            input_error = 1

    context = {'input_error': input_error}
    return render(request, 'index_2.html', context)


#
def index_2_1(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = None
    if request.method == RequestMethod.POST:
        auth_form = AuthUserForm(request.POST)
        if auth_form.is_valid():
            user = CustomUser.objects.filter(
                inn=auth_form.data.get('inn'),
                username=auth_form.data.get('eded@cfdd')
            ).first()
            if user:
                login(request, user)
                return redirect('redirect')
            else:
                return redirect('index_3_1')

        else:
            error_msg = 'Ошибка ввода'

    inn = request.GET.get('inn', '')
    context = {'inn': inn, 'error_msg': error_msg}
    return render(request, 'index_2_1.html', context)


# регистрация заполните форму
def index_3_1(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        reg_form = RegistrationForm(request.POST)

        if reg_form.is_valid():
            password = pass_gen()
            log_error(f'>>>>>> {password}', wt=False)
            #  тут пароль отправляем на почту
            new_user = CustomUser(
                username=reg_form.cleaned_data['email'],
                inn=reg_form.cleaned_data['inn'],
                full_name=reg_form.cleaned_data['fio'],
                phone=reg_form.cleaned_data['tel'],
                password=make_password(password)
            )
            new_user.save()

            return redirect(reverse('index_2_2') + f'?user={new_user.id}')

    prods = [
        {'name': 'ПО 1', 'id': 1},
        {'name': 'ПО 2', 'id': 2},
        {'name': 'ПО 3', 'id': 3},
    ]
    context = {'prods': prods}
    return render(request, 'index_3_1.html', context)


# принимает пароль и регистрирует пользователя
# kP4f2PwD
def index_2_2(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = None
    if request.method == RequestMethod.POST:
        pass_form = PasswordForm(request.POST)
        log_error(f'>>>>>> {pass_form.is_valid()}', wt=False)
        if pass_form.is_valid():
            user_id = request.POST.get('user_id')
            # user = CustomUser.objects.filter(id=user_id).first()
            user = CustomUser.objects.get(id=user_id)
            if check_password(pass_form.cleaned_data['password'], user.password):
                login(request, user)
                return redirect('redirect')

            else:
                error_msg = 'Неверный пароль'

    user_id = request.GET.get('user')
    context = {
        'error_msg': error_msg,
        'user_id': user_id
    }
    return render(request, 'index_2_2.html', context)
