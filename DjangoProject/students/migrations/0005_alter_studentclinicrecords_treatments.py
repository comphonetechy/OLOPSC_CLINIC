# Generated by Django 4.1.5 on 2023-01-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_studentclinicrecords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclinicrecords',
            name='treatments',
            field=models.CharField(max_length=30),
        ),
    ]
