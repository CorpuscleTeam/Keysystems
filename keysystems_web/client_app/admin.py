from django.contrib import admin

from .models import News


# админка новости
@admin.register(News)
class ViewAdminNews(admin.ModelAdmin):
    list_display = ['type_entry', 'title', 'photo', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']
