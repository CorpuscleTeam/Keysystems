from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserKS


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=(
            "Пороль храниться в хешированом виде. Чтоб изменить пароль воспользуйтесь  "
            "<a href=\"../password/\">формой</a>."
        ),
    )

    class Meta:
        model = UserKS
        fields = ('username', 'email', 'password', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]