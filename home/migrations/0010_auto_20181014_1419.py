# Generated by Django 2.1.2 on 2018-10-14 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_hostel_adminphoneno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostel',
            old_name='AdminPhoneNo',
            new_name='PhoneNo',
        ),
    ]