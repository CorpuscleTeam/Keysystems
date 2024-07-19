# Generated by Django 5.0.6 on 2024-07-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлена')),
                ('type_entry', models.CharField(choices=[('news', 'Новость'), ('update', 'Обновление ПО')], max_length=50, verbose_name='Тип')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='автор')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text_preview', models.TextField(blank=True, null=True, verbose_name='Текст привью')),
                ('text', models.TextField(verbose_name='Текст')),
                ('photo', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
    ]
