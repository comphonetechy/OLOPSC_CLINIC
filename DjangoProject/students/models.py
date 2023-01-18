from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30,verbose_name="First name")
    last_name = models.CharField(max_length=30,verbose_name="Last name")
    student_number = models.IntegerField(max_length=30)
    guardian_name = models.CharField(max_length=30)
    guardian_contact = models.CharField(max_length=30)
    user_created = models.CharField(max_length=30, default="2023")
    #BACKGROUND HEALTH
    def __str__(self):
        return self.first_name + " " + self.last_name
""" chickenpox
    dengue
    diphtheria
    germanmeasles
    hepatitis
    measles
    mumps
    primarycomplex
    typhoidfever
    whoopingcough
    asthma
    diabetes
    eardisorder
    epilepsy
    eyedisorder
    hearthdisease
    kidneydisease
    tuberculosis
    g6pd
    othersspecify
    #PERMISSION GRANTED FOR (PLEASE CHECK)
    treatment_of_sudden_illness_or_injuries
    giving_initial_medication
    take_to_hospital_if_emergency"""





class DailyClinicRecords(models.Model):
    date_and_time_of_visit = models.CharField(max_length=30)
    student_name = models.CharField(max_length=30)
    student_number = models.IntegerField(max_length=30)
    year_level_and_course = models.CharField(max_length=30)


class StudentClinicRecords(models.Model):
    student_record = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_rec")
    date_and_time_of_visit = models.CharField(max_length=30)
    chief_complaints = models.CharField(max_length=30)
    treatments = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)

def __str__(self):
    return self.student_record
