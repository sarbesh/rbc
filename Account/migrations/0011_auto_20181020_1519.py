# Generated by Django 2.1.2 on 2018-10-20 09:49

import Account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0010_auto_20181020_1519'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='rbcuser',
            managers=[
                ('objects', Account.models.RBCUserManager()),
            ],
        ),
    ]