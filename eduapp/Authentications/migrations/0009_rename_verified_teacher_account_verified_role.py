# Generated by Django 4.1.4 on 2022-12-29 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentications', '0008_alter_account_date_of_birth_alter_account_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='verified_teacher',
            new_name='verified_role',
        ),
    ]
