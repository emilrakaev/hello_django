# Generated by Django 2.2 on 2020-08-06 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20200806_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tags_old',
        ),
    ]
