# Generated by Django 4.1.5 on 2023-01-15 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_studentclinicrecords_treatments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentclinicrecords',
            name='student_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis', to='students.student'),
        ),
    ]
