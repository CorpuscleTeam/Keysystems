from django.contrib import admin

from .models import Soft, Customer, OrderTopic, UserKS
from .forms import CustomUserChangeForm


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields + ('email',)  # Добавьте дополнительные поля, если нужно
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields


# админка софт
@admin.register(UserKS)
class ViewAdminUser(admin.ModelAdmin):
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'is_active', 'is_staff']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
    # list_display = ['inn', 'full_name', 'username', 'phone', 'is_staff']
    # readonly_fields = ['date_joined', 'last_login']
    #
    # def get_fields(self, request, obj=None):
    #     fields = super().get_fields(request, obj)
    #     # Удаляем поле 'photo' из списка полей
    #     fields.remove('email')
    #     fields.remove('last_name')
    #     fields.remove('first_name')
    #     return fields


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
