# Generated by Django 4.1.4 on 2023-02-01 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=300)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.ForeignKey(default='Portland', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='app.city', to_field='name')),
            ],
        ),
    ]
