# Generated by Django 4.1.5 on 2023-01-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_dailyclinicrecords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyclinicrecords',
            name='date_and_time_of_visit',
            field=models.CharField(max_length=30),
        ),
    ]
