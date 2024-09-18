from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from keysystems_web.settings import DEBUG
from . import models as m
from common.logs import log_error


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = m.UserKS
        fields = UserCreationForm.Meta.fields + ('email',)  # Добавьте дополнительные поля, если нужно


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = m.UserKS
        fields = UserChangeForm.Meta.fields


class SoftBSmartInline(admin.TabularInline):
    model = m.SoftBSmart
    extra = 0


class SoftAdminDInline(admin.TabularInline):
    model = m.SoftAdminD
    extra = 0


class SoftSSmartInline(admin.TabularInline):
    model = m.SoftSSmart
    extra = 0


class SoftPSmartInline(admin.TabularInline):
    model = m.SoftPSmart
    extra = 0


class SoftWebTInline(admin.TabularInline):
    model = m.SoftWebT
    extra = 0


class SoftDigitBInline(admin.TabularInline):
    model = m.SoftDigitB
    extra = 0


class SoftOSmartInline(admin.TabularInline):
    model = m.SoftOSmart
    extra = 0


class SoftExceptionsInline(admin.TabularInline):
    model = m.SoftExceptions
    extra = 0


# админка софт
@admin.register(m.UserKS)
class ViewAdminUser(admin.ModelAdmin):
    inlines = [
        SoftBSmartInline,
        SoftAdminDInline,
        SoftSSmartInline,
        SoftPSmartInline,
        SoftWebTInline,
        SoftDigitBInline,
        SoftOSmartInline,
        SoftExceptionsInline
    ]

    form = CustomUserChangeForm
    list_display = ['full_name', 'username', 'phone', 'is_staff']
    readonly_fields = ['last_login', 'date_joined']
    ordering = ['-is_staff']

    fieldsets = (
        ('О пользователе', {'fields': ('full_name', 'username', 'phone', 'inn')}),
        ('Права', {'fields': ('is_staff', 'is_superuser')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
    )

    # Переопределяем метод для управления инлайнами
    def get_inline_instances(self, request, obj=None):
        # Получаем стандартный список инлайнов
        inline_instances = []
        # log_error(f'{obj}', wt=False)
        # Проверяем, является ли пользователь персоналом
        if obj and obj.is_staff:
            # Добавляем только если это сотрудник
            inline_instances = super().get_inline_instances(request, obj)
        return inline_instances

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        # Если пользователь является персоналом, заменяем customer на inn
        if not obj or obj.is_staff:
            fieldsets[0][1]['fields'] = ('full_name', 'username', 'phone', 'inn')
        else:
            fieldsets[0][1]['fields'] = ('full_name', 'username', 'phone', 'customer')

        return fieldsets


# админка софт
# @admin.register(m.Soft)
# class ViewAdminSoft(admin.ModelAdmin):
#     list_display = ['title', 'description', 'is_active']

    # def event_name(self, obj):
    #     event = Event.objects.filter(id=obj.event_id).first()
    #     return event.title if event else str(obj.event_id)
    #
    # event_name.short_description = 'Ивент'


# админка темы обращений
# @admin.register(m.OrderTopic)
# class ViewAdminOrderTopic(admin.ModelAdmin):
#     list_display = ['topic', 'is_active']
#     list_editable = ['is_active']


# админка темы обращений
@admin.register(m.Customer)
class ViewAdminCostumer(admin.ModelAdmin):
    list_display = ['inn', 'title', 'district']
    readonly_fields = ['created_at', 'updated_at']


class OrderCuratorInline(admin.TabularInline):
    model = m.OrderCurator
    extra = 1

    # Переопределяем поле 'user' для фильтрации
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            # Фильтруем только пользователей со статусом персонала
            kwargs['queryset'] = m.UserKS.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OrderFilesInline(admin.TabularInline):
    model = m.DownloadedFile
    fields = ['url', 'file_size']
    extra = 1


# админка обращения
@admin.register(m.Order)
class ViewAdminOrder(admin.ModelAdmin):
    inlines = [OrderCuratorInline, OrderFilesInline]
    list_display = ['id', 'from_user', 'soft', 'topic', 'text', 'status']
    list_editable = ['from_user', 'status']
    readonly_fields = ['created_at', 'updated_at']


# # админка районы
@admin.register(m.District)
class ViewAdminNews(admin.ModelAdmin):
    list_display = ['title']


# # админка уведомления
if DEBUG:
    @admin.register(m.Notice)
    class ViewAdminNews(admin.ModelAdmin):
        list_display = ['text']


# сообщения
if DEBUG:
    @admin.register(m.Message)
    class ViewAdminNews(admin.ModelAdmin):
        list_display = ['created_at', 'from_user', 'chat', 'text']
