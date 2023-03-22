# Generated by Django 4.1.4 on 2023-02-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_city_name_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('users', models.ManyToManyField(blank=True, null=True, related_name='friends', to='app.contact')),
            ],
        ),
    ]
