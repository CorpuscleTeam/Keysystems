from django import forms


# проверка инн
class OrderForm(forms.Form):
    type_appeal = forms.IntegerField()
    type_soft = forms.IntegerField()
    description = forms.CharField()
    addfile = forms.FileField()
