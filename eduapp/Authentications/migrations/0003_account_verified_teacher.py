# Generated by Django 4.1.4 on 2022-12-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentications', '0002_account_is_student_account_is_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='verified_teacher',
            field=models.BooleanField(default=False),
        ),
    ]
