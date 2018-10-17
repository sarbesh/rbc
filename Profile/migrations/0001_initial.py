# Generated by Django 2.1.2 on 2018-10-15 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_status', models.BooleanField(default=True)),
                ('veg_on_egg', models.BooleanField(default=False)),
                ('veg_on_fish', models.BooleanField(default=False)),
                ('veg_on_chicken', models.BooleanField(default=False)),
                ('veg_on_mutton', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserDetails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]