# Generated by Django 2.1.2 on 2018-10-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20181014_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_upload',
            name='image_slug',
            field=models.CharField(default='R.B.C Hall', help_text='slug to identify image for seo, keep different', max_length=10),
        ),
    ]