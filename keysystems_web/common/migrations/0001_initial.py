# Generated by Django 5.0.6 on 2024-07-17 14:05

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 17, 23, 5, 17, 971198), verbose_name='Создана')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 7, 17, 23, 5, 17, 971214), verbose_name='Обновлена')),
                ('inn', models.BigIntegerField(blank=True, null=True, verbose_name='ИНН')),
                ('district', models.CharField(max_length=255, verbose_name='Текст')),
                ('title', models.CharField(max_length=255, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='OrderTopic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Тема обращения',
                'verbose_name_plural': 'Темы обращений',
                'db_table': 'orders_topics',
            },
        ),
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ПО',
                'verbose_name_plural': 'ПО',
                'db_table': 'soft',
            },
        ),
        migrations.CreateModel(
            name='UserKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('inn', models.BigIntegerField(blank=True, null=True, verbose_name='ИНН')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Почта')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set', related_query_name='customuser', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set', related_query_name='customuser', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 17, 23, 5, 17, 969990), verbose_name='Создана')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 7, 17, 23, 5, 17, 970012), verbose_name='Обновлена')),
                ('text', models.CharField(max_length=255, verbose_name='Текст')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('active', 'В работе'), ('done', 'Активный')], default='new', verbose_name='Статус')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='executed_orders', to=settings.AUTH_USER_MODEL)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_orders', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='common.ordertopic')),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='common.soft')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='DownloadedFile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 7, 17, 23, 5, 17, 970720), verbose_name='Создана')),
                ('url', models.CharField(choices=[('new', 'Новый'), ('active', 'В работе'), ('done', 'Активный')], default='new', max_length=255, verbose_name='Ссылка')),
                ('user_ks', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='downloadedfile', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloadedfile', to='common.order')),
            ],
            options={
                'verbose_name': 'Скаченный файл',
                'verbose_name_plural': 'Скаченные файлы',
                'db_table': 'downloaded_file',
            },
        ),
        migrations.CreateModel(
            name='UsedSoft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('soft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_soft', to='common.soft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_soft', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ПО пользователей',
                'verbose_name_plural': 'ПО пользователей',
                'db_table': 'used_soft',
            },
        ),
    ]
