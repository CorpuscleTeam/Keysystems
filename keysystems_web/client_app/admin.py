from django.contrib import admin
from django.utils.html import mark_safe

from .models import News, FAQ, UpdateSoft, UpdateSoftFiles


# админка новости
@admin.register(News)
class ViewAdminNews(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'cover_image_preview']
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


# вопросы
@admin.register(FAQ)
class ViewAdminFAQ(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_active']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active']


class UpdateSoftFilesInline(admin.TabularInline):
    model = UpdateSoftFiles
    extra = 1


@admin.register(UpdateSoft)
class RecordAdmin(admin.ModelAdmin):
    inlines = [UpdateSoftFilesInline]
    list_display = ['soft', 'description']
    readonly_fields = ['created_at', 'updated_at']
