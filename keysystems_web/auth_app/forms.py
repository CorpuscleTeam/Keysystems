from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserKS


# проверка инн
class AuthBaseForm(forms.Form):
    inn = forms.IntegerField()


# проверка инн + почта
class AuthUserForm(forms.Form):
    inn = forms.IntegerField()
    email = forms.EmailField()


# проверка пароля
class PasswordForm(forms.Form):
    password = forms.CharField()


# форма регистрации
class RegistrationForm(forms.Form):
    # inn = forms.IntegerField(min_value=1000000000, max_value=999999999999)
    inn = forms.IntegerField()
    email = forms.CharField()
    fio = forms.CharField()
    tel = forms.CharField()
    reg_progr = forms.CharField(empty_value='1')

'''
2024-07-10 15:49:41 <QueryDict: {'csrfmiddlewaretoken': ['Lgu0Ze4EmLNwFrqrRa94TE3bTKkBKLdP0fDaibD09LEChRAzhtXbLIkdTytlubx4'], 
'inn': ['5555'], 'reg_progr': [''], 'email': ['ggggg@fffff'], 'fio': ['fggg'], 'tel': ['55555']}
'''

    # class Meta:
    #     model = UserKS
    #     fields = ('inn', 'email', 'full_name', 'phone')
