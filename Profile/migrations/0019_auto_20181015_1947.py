# Generated by Django 2.1.2 on 2018-10-15 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0018_auto_20181015_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserDetails', to=settings.AUTH_USER_MODEL),
        ),
    ]
