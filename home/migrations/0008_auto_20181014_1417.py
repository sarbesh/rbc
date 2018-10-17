# Generated by Django 2.1.2 on 2018-10-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20181013_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Hostel/Images/')),
                ('image_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='hostel',
            name='Facebook',
            field=models.URLField(default='https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/', help_text='url to facebook page, default = https://www.facebook.com/Rishi-Bankim-Chandra-HallKGEC-105289579543000/ '),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Google_Plus',
            field=models.URLField(default='https://plus.google.com/u/5/', help_text='google+ default url:- https://plus.google.com/u/5/'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Twitter',
            field=models.URLField(default='https://twitter.com/kgecrbchall', help_text='twitter link, default = https://twitter.com/kgecrbchall'),
        ),
        migrations.AddField(
            model_name='hostel',
            name='Youtube',
            field=models.URLField(default='https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA', help_text='youtube channel default:-https://www.youtube.com/channel/UC3JOr-Opub8GRKwJjktqZtA'),
        ),
    ]
