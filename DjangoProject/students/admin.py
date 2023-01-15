from django.contrib import admin
from .models import Student, DailyClinicRecords

# Register your models here.

admin.site.site_header = "OLOPSC CLINIC"
admin.site.site_title = "OLOPSC CLINIC"
admin.site.index_title = "Welcome to OLOPSC CLINIC!"

class StudentInfo(admin.ModelAdmin):
    list_display = ['first_name','last_name','student_number','guardian_name','guardian_contact']

class ClinicVisitors(admin.ModelAdmin):
    list_display = ['date_and_time_of_visit','student_name','student_number','year_level_and_course']

admin.site.register(Student, StudentInfo)
admin.site.register(DailyClinicRecords, ClinicVisitors)
