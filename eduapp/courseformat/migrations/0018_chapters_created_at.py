# Generated by Django 4.1.4 on 2023-01-25 05:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courseformat', '0017_chaptermaterials_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
