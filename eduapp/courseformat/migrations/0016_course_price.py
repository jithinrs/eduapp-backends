# Generated by Django 4.1.4 on 2023-01-22 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseformat', '0015_chaptermaterials_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]