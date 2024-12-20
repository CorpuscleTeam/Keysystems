from pathlib import Path
from logging.handlers import TimedRotatingFileHandler

import os
import redis


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_KEY')
DEBUG = bool(int(os.getenv('DEBUG')))
# DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_ckeditor_5',
    'channels',
    'common',
    'client_app',
    'auth_app',
    'curator_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'keysystems_web.urls'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_PORT = 587
EMAIL_USE_TLS = True
# Для gmail
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'dgushch@gmail.com'
# EMAIL_HOST_PASSWORD = 'vgjk cqkb iqbu mzoj'

# Для mail.ru
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')


# EMAIL_HOST = 'smtp.mail.ru'
# EMAIL_HOST_USER = 'lkyktks@mail.ru'
# EMAIL_HOST_PASSWORD = 'iKed5x0Djc5qX6YCLHYj'
# DEFAULT_FROM_EMAIL = 'lkyktks@mail.ru'

'''
smtp.nicmail.ru
postmaster@h202060049.nichost.ru
Qwerty12

4087971/NIC-D
123456
'''

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'keysystems_web.wsgi.application'
ASGI_APPLICATION = "keysystems_web.asgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }}

REDIS_DB = redis.Redis(host=os.getenv('DB_HOST'), port=6379, db=0)
REDIS_TTL: int = 60 * 60  # один час

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yakutsk'

USE_I18N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Сессия сохраняется при закрытии браузера
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365  # год

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
if not os.path.exists(STATIC_ROOT):
    os.mkdir(STATIC_ROOT)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

FILE_STORAGE = os.path.join(MEDIA_ROOT, 'downloaded_files')
if not os.path.exists(FILE_STORAGE):
    os.mkdir(FILE_STORAGE)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'common.UserKS'

CKEDITOR_UPLOAD_PATH = "ck_storage/"

LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            # 'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'WARNING',
            'propagate': True,
        },
        'channels': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis_ks', 6379)],
        },
    },
}


# редактор текста в админке
DJANGO_CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 500,
        'width': 'auto',
        'remove_plugins': 'stylesheetparser',
        'extra_plugins': ','.join([
            'uploadimage',  # Для загрузки изображений
            'basicstyles',  # Простые стили (жирный, курсив)
            # Добавьте сюда дополнительные плагины, если нужно
        ]),
    },
}
# CK_EDITOR_5_UPLOAD_FILE_VIEW_NAME = "media"
CKEDITOR_5_CUSTOM_CSS = 'path_to.css'  # optional
CKEDITOR_5_CONFIGS = {
    'default': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['bold', 'italic', 'link', 'underline', 'strikethrough',
                    'code', 'subscript', 'superscript', 'highlight'
                    ],
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}
