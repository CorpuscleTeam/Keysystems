from django.apps import AppConfig


class ClientAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_app'
    verbose_name = 'Клиент'
    verbose_name_plural = 'Клиент'
