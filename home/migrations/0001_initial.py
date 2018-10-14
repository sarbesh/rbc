# Generated by Django 2.1.2 on 2018-10-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('Hostel_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Hostel_Email', models.EmailField(default='', max_length=254)),
                ('Hostel_startdate', models.DateField()),
                ('Hostel_logo', models.ImageField(height_field=150, upload_to='Hostel/Logo/', width_field=500)),
                ('Hostel_description', models.TextField()),
                ('Hostel_Images', models.ImageField(height_field=300, upload_to='Hostel/Images/', width_field=700)),
            ],
        ),
    ]
