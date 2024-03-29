# Generated by Django 4.1.6 on 2023-02-16 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_shorturl_host_header_shorturl_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='host_header',
        ),
        migrations.RemoveField(
            model_name='shorturl',
            name='ip_address',
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_header', models.CharField(blank=True, max_length=30)),
                ('ip_address', models.CharField(blank=True, max_length=30)),
                ('short_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.shorturl')),
            ],
        ),
    ]
