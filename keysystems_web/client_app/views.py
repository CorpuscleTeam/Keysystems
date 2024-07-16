from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize

import os

from keysystems_web.settings import FILE_STORAGE
from .forms import OrderForm
from .models import news, OrderTopic, Soft
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
        log_error(request.FILES, wt=False)
        # log_error(request.POST, wt=False)
        # log_error(order_form.is_valid(), wt=False)
        if order_form.is_valid():
            topic_id = order_form.cleaned_data['type_appeal']
            soft_id = order_form.cleaned_data['type_soft']
            description = order_form.cleaned_data['description']
            file = order_form.cleaned_data.get('addfile')

            files = request.FILES.getlist('addfile')
            log_error(f'{len(files), files}', wt=False)

            # uploaded_file = request.FILES['addfile']
            folder_path = os.path.join(FILE_STORAGE, str(request.user.inn))
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            fs = FileSystemStorage()
            for uploaded_file in files:
                file_path = os.path.join(folder_path, uploaded_file.name)
                filename = fs.save(file_path, uploaded_file)
                file_url = fs.url(filename)

                log_error(f'{file_url}', wt=False)
            # log_error(f'{topic_id}\n{soft_id}\n{description}\n{file}', wt=False)

    topics = OrderTopic.objects.filter(is_active=True).all()
    soft = Soft.objects.filter(is_active=True).all()
    soft_json = serialize('json', soft)
    topics_json = serialize('json', topics)
    context = {
        'news': news,
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
