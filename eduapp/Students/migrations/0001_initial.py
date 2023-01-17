# Generated by Django 4.1.4 on 2022-12-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('grade', models.CharField(choices=[('8', '8th grade'), ('9', '9th grade'), ('10', '10th grade'), ('11', '11th grade'), ('12', '12th grade')], max_length=3)),
                ('school_name', models.CharField(max_length=255)),
                ('school_address', models.CharField(max_length=511)),
                ('home_address', models.CharField(max_length=511)),
                ('guardian', models.CharField(max_length=127)),
                ('guardian_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
    ]