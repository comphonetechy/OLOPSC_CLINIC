from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    student_number = models.IntegerField(max_length=30)
    guardian_name = models.CharField(max_length=30)
    guardian_contact = models.CharField(max_length=30)  

def __str__(self):
    return self.first_name

class DailyClinicRecords(models.Model):
    date_and_time_of_visit = models.CharField(max_length=30)
    student_name = models.CharField(max_length=30)
    student_number = models.IntegerField(max_length=30)
    year_level_and_course = models.CharField(max_length=30)
