# Generated by Django 4.1.4 on 2022-12-26 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0004_teachercredentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachercredentials',
            name='status_approved',
            field=models.BooleanField(default=False),
        ),
    ]
