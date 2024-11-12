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
    fields = ('prefix', 'ministry')
    model = m.SoftBSmart
    extra = 0


class SoftAdminDInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftAdminD
    extra = 0


class SoftSSmartInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftSSmart
    extra = 0


class SoftPSmartInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftPSmart
    extra = 0


class SoftWebTInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftWebT
    extra = 0


class SoftDigitBInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftDigitB
    extra = 0


class SoftOSmartInline(admin.TabularInline):
    fields = ('prefix', 'ministry')
    model = m.SoftOSmart
    extra = 0


class SoftExceptionsInline(admin.TabularInline):
    model = m.SoftExceptions
    extra = 0
    # autocomplete_fields = ['title']  # Включает поиск для внешнего ключа



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
    search_fields = ['full_name', 'inn', 'customer', 'title']
    list_filter = ['is_staff']

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


# админка темы обращений
@admin.register(m.Customer)
class ViewAdminCostumer(admin.ModelAdmin):
    list_display = ['inn', 'title']
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
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ['id']
    list_filter = ['topic', 'soft', 'status']


@admin.register(m.Ministry)
class ViewAdminMinistry(admin.ModelAdmin):
    list_display = ['name']
    readonly_fields = ['created_at', 'updated_at']


# # админка уведомления
if DEBUG:
    @admin.register(m.Notice)
    class ViewAdminNotice(admin.ModelAdmin):
        list_display = ['text']


# сообщения
if DEBUG:
    @admin.register(m.Message)
    class ViewAdminMessage(admin.ModelAdmin):
        list_display = ['created_at', 'from_user', 'chat', 'text']
