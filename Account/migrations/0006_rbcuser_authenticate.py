# Generated by Django 2.1.2 on 2018-10-19 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20181017_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbcuser',
            name='authenticate',
            field=models.BooleanField(default=False),
        ),
    ]
