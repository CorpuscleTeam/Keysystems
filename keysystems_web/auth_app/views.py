from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

from .forms import AuthBaseForm, RegistrationForm, PasswordForm, AuthUserForm
from common.models import UserKS, Soft, Customer
from keysystems_web.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from base_utils import log_error, pass_gen, send_pass_email
from enums import RequestMethod, UserRole


# Определяет начальную страницу пользователя
def start_page_redirect(request: HttpRequest):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('index_4_1')

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
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = ''
    if request.method == RequestMethod.POST:
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            input_inn = form.cleaned_data["inn"]
            users_inn = UserKS.objects.filter(inn=input_inn).all()

            if len(users_inn) == 0:
                inn = Customer.objects.filter(inn=input_inn)
                if inn:
                    return redirect('index_3_1')
                else:
                    error_msg = 'ИНН не зарегистрирован'

            elif len(users_inn) == 1:
                return redirect(reverse('index_3_1'))

            elif len(users_inn) > 1:
                return redirect(reverse('index_2_1') + f'?inn={users_inn}')

            else:
                return redirect('index_2_2')
        else:
            error_msg = 'Ошибка ввода'

    context = {'error_msg': error_msg}
    return render(request, 'index_2.html', context)


#
def index_2_1(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = None
    if request.method == RequestMethod.POST:
        auth_form = AuthUserForm(request.POST)
        if auth_form.is_valid():
            user = UserKS.objects.filter(
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
    # if request.user.is_authenticated:
    #     return redirect('redirect')

    if request.method == RequestMethod.POST:
        reg_form = RegistrationForm(request.POST)
        log_error(f'>>>>>> {request.POST}', wt=False)
        if reg_form.is_valid():
            password = pass_gen()
            log_error(f'>>>>>> {password}', wt=False)
            log_error(f'>>>>>> {reg_form.cleaned_data["reg_progr"]}', wt=False)

            #  тут пароль отправляем на почту
            send_pass_email(email=reg_form.cleaned_data['email'], password=password)

            new_user = UserKS(
                username=reg_form.cleaned_data['email'],
                inn=reg_form.cleaned_data['inn'],
                full_name=reg_form.cleaned_data['fio'],
                phone=reg_form.cleaned_data['tel'],
                password=make_password(password)
            )
            new_user.save()

            return redirect(reverse('index_2_2') + f'?user={new_user.id}')

    soft = Soft.objects.filter(is_active=True).all()
    context = {'soft': soft}
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
            user = UserKS.objects.get(id=user_id)
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
