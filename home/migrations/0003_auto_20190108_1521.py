# Generated by Django 2.1.2 on 2019-01-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190108_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aaa',
            name='Event_Image',
            field=models.ImageField(blank=True, default='image.png', null=True, upload_to='AAA/'),
        ),
    ]
