from django.contrib import admin
from django.utils.html import mark_safe

import os

from .models import News
from base_utils import log_error


# админка новости
@admin.register(News)
class ViewAdminNews(admin.ModelAdmin):
    list_display = ['type_entry', 'title', 'is_active', 'cover_image_preview']
    readonly_fields = ['created_at', 'updated_at', 'cover_image_preview_in']
    list_editable = ['is_active']

    def cover_image_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-width:100px; max-height:100px;">')
        else:
            return "No image"

    def cover_image_preview_in(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="max-width:300px; max-height:300px;">')
        else:
            return "No image"

    cover_image_preview.short_description = 'Фото'
    cover_image_preview_in.short_description = 'Фото'

