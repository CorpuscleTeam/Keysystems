from django.contrib import admin

from .models import Soft, Customer, OrderTopic
from client_app.models import News


# админка софт
@admin.register(Soft)
class ViewAdminSoft(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_active']

    # def event_name(self, obj):
    #     event = Event.objects.filter(id=obj.event_id).first()
    #     return event.title if event else str(obj.event_id)
    #
    # event_name.short_description = 'Ивент'


# админка темы обращений
@admin.register(OrderTopic)
class ViewAdminOrderTopic(admin.ModelAdmin):
    list_display = ['topic', 'is_active']
    list_editable = ['is_active']


# админка темы обращений
@admin.register(Customer)
class ViewAdminCostumer(admin.ModelAdmin):
    list_display = ['inn', 'district', 'title']
    readonly_fields = ['created_at', 'updated_at']


# # админка новости
# @admin.register(News)
# class ViewAdminNews(admin.ModelAdmin):
#     list_display = ['type_entry', 'title', 'photo', 'is_active']
#     readonly_fields = ['created_at', 'updated_at']
#     list_editable = ['is_active']
