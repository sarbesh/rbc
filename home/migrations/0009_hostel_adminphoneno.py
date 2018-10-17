# Generated by Django 2.1.2 on 2018-10-14 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20181014_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='AdminPhoneNo',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.", regex='^\\+?1?\\d{10,13}$')]),
        ),
    ]
