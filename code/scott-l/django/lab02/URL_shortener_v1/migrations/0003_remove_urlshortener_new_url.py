# Generated by Django 4.1.7 on 2023-02-22 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URL_shortener_v1', '0002_urlshortener_new_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlshortener',
            name='new_URL',
        ),
    ]