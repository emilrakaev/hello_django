# Generated by Django 2.2 on 2020-07-29 17:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200722_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Время публикации'),
        ),
    ]