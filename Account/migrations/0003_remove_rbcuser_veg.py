# Generated by Django 2.1.2 on 2018-10-17 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20181015_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rbcuser',
            name='veg',
        ),
    ]
