# Generated by Django 4.1.4 on 2023-02-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortener',
            name='times_followed',
            field=models.PositiveIntegerField(default=0),
        ),
    ]