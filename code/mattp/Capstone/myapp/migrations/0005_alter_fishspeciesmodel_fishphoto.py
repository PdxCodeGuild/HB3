# Generated by Django 4.1.7 on 2023-03-25 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_fishspeciesmodel_fish_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishspeciesmodel',
            name='fishphoto',
            field=models.ImageField(default=0, upload_to='static/'),
        ),
    ]