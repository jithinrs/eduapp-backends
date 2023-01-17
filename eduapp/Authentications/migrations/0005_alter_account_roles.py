# Generated by Django 4.1.4 on 2022-12-28 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentications', '0004_remove_account_is_student_remove_account_is_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='roles',
            field=models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], max_length=1, null=True),
        ),
    ]
