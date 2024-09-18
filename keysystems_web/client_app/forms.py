from django import forms


# проверка инн
class OrderForm(forms.Form):
    type_form = forms.CharField()
    type_appeal = forms.CharField()
    type_soft = forms.CharField()
    description = forms.CharField()
    fullDescription = forms.CharField()
    addfile = forms.FileField(required=False)


class UserSettingForm(forms.Form):
    type_soft = forms.CharField()
    settings_email = forms.EmailField()
    settings_responsible = forms.CharField()
    settings_phone = forms.CharField()

# 'type_soft': ['1'], 'settings_email': [''], 'settings_responsible': [''], 'settings_phone': ['']}>
