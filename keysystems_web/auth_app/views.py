from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.core.serializers import serialize

from .forms import AuthBaseForm, RegistrationForm, PasswordForm, AuthUserForm
from common.models import UserKS, Soft, Customer, District, UsedSoft
from common import log_error, pass_gen, send_pass_email, yakutia_districts
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


# заглушка
def indev_view(request):
    context = {}
    return render(request, 'in_dev.html', context)


# первая клиентская страница. Просит инн
def index_2(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = ''
    if request.method == RequestMethod.POST:
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            input_inn = form.cleaned_data["inn"]
            costumer = Customer.objects.get(inn=input_inn)
            users_inn = UserKS.objects.filter(customer=costumer).all()
            log_error(f'>>len(users_inn): {len(users_inn)}', wt=False)

            if len(users_inn) == 0:
                if costumer:
                    return redirect(reverse('index_3_1') + f'?inn={input_inn}')
                else:
                    error_msg = 'ИНН не зарегистрирован'

            elif len(users_inn) == 1:
                return redirect(reverse('index_2_2') + f'?inn={input_inn}')

            elif len(users_inn) > 1:
                return redirect(reverse('index_2_1') + f'?inn={input_inn}')

            else:
                return redirect('index_2_2')
        else:
            error_msg = 'Ошибка ввода'

    context = {'error_msg': error_msg}
    return render(request, 'auth/index_2.html', context)


#
def index_2_1(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    error_msg = ''
    if request.method == RequestMethod.POST:
        auth_form = AuthUserForm(request.POST)
        if auth_form.is_valid():
            customer = Customer.objects.get(inn=auth_form.cleaned_data['inn'])
            user = UserKS.objects.filter(
                customer=customer,
                username=auth_form.cleaned_data['email']
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
    return render(request, 'auth/index_2_1.html', context)


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
    return render(request, 'auth/index_2_2.html', context)


# регистрация заполните форму
def index_3_1(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('redirect')

    if request.method == RequestMethod.POST:
        # log_error(request.POST, wt=False)
        reg_form = RegistrationForm(request.POST)
        inn = Customer.objects.filter(inn=reg_form.data.get('inn', 0))
        if reg_form.is_valid() and inn:

            password = pass_gen()
            #  тут пароль отправляем на почту
            send_pass_email(email=reg_form.cleaned_data['email'], password=password)

            new_user = UserKS(
                username=reg_form.cleaned_data['email'],
                customer=Customer.objects.get(inn=reg_form.cleaned_data['inn']),
                full_name=reg_form.cleaned_data['fio'],
                phone=reg_form.cleaned_data['tel'],
                password=make_password(password)
            )
            new_user.save()

            used_soft = Soft.objects.get(id=reg_form.cleaned_data['reg_progr'])
            UsedSoft.objects.create(user=new_user, soft=used_soft)
            return redirect(reverse('index_2_2') + f'?user={new_user.pk}')

    context = {
        'soft': serialize(format='json', queryset=Soft.objects.filter(is_active=True).all()),
        'inn': request.GET.get('inn', '')
    }
    return render(request, 'auth/index_3_1.html', context)
