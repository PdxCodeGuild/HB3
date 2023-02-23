# Generated by Django 4.1.4 on 2023-02-18 01:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='date_completed',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='list',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]