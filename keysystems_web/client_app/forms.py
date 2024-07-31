from django import forms


# проверка инн
class OrderForm(forms.Form):
    type_form = forms.CharField()
    type_appeal = forms.IntegerField()
    type_soft = forms.IntegerField()
    description = forms.CharField()
    addfile = forms.FileField(required=False)


class UserSettingForm(forms.Form):
    type_soft = forms.IntegerField()
    settings_email = forms.EmailField()
    settings_responsible = forms.CharField()
    settings_phone = forms.CharField()

# 'type_soft': ['1'], 'settings_email': [''], 'settings_responsible': [''], 'settings_phone': ['']}>
