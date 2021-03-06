# Generated by Django 3.0.11 on 2020-11-23 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201120_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/users')),
                ('birth_day', models.DateField(blank=True, default=None, null=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('resume', models.TextField(blank=True)),
                ('company', models.CharField(blank=True, max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
