from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize

import os

from keysystems_web.settings import FILE_STORAGE
from .forms import OrderForm
from .models import News
from common.models import OrderTopic, Soft, Order, DownloadedFile
from base_utils import log_error
from enums import RequestMethod


# удалить аналог 2_2
def index_3_2(request: HttpRequest):
    context = {}
    return render(request, 'index_3_2.html', context)

'''
'type_appeal': ['1'], 
'type_soft': ['1'], 
'description': ['уаккав'], 
'addfile': ['Снимок экрана 2024-05-25 162508.png']}>
'''


# страничка с новостями
def index_4_1(request: HttpRequest):
    if request.method == RequestMethod.POST:
        order_form = OrderForm(request.POST, request.FILES)
        # log_error(request.FILES, wt=False)
        log_error(request.POST, wt=False)
        log_error(order_form, wt=False)
        if order_form.is_valid():
            new_order = Order(
                from_user=request.user.pk,
                text=order_form.cleaned_data['description'],
                soft=order_form.cleaned_data['type_soft'],
                topic=order_form.cleaned_data['type_appeal']
            )
            new_order.save()

            files = request.FILES.getlist('addfile')
            log_error(f'{len(files), files}', wt=False)

            folder_path = os.path.join(FILE_STORAGE, str(request.user.inn), str(new_order.pk))
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            fs = FileSystemStorage()
            for uploaded_file in files:
                file_path = os.path.join(folder_path, uploaded_file.name)
                filename = fs.save(file_path, uploaded_file)
                file_url = fs.url(filename)

                DownloadedFile.objects.create(
                    user_ks=request.user.pk,
                    order=new_order.pk,
                    url=file_url
                )
            return redirect('redirect')

    soft_json = serialize(format='json', queryset=Soft.objects.filter(is_active=True).all())
    topics_json = serialize(format='json', queryset=OrderTopic.objects.filter(is_active=True).all())
    news_json = serialize(format='json', queryset=News.objects.filter(is_active=True).all())
    context = {
        'news': news_json,
        'topics': topics_json,
        'soft': soft_json,
        'orders_count': 3,
        'notice': 10,
        'update_count': 44,
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_4_2.html', context)
