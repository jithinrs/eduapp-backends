# Generated by Django 4.1.4 on 2022-12-31 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0013_remove_teachercredentials_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachercredentials',
            name='teacher_name',
        ),
    ]
