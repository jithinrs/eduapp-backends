# Generated by Django 4.1.4 on 2023-01-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseformat', '0012_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]