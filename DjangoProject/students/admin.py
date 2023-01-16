from django.contrib import admin
from .models import Student, DailyClinicRecords, StudentClinicRecords

# Register your models here.

admin.site.site_header = "OLOPSC CLINIC"
admin.site.site_title = "OLOPSC CLINIC"
admin.site.index_title = "Welcome to OLOPSC CLINIC!"

class StudentInfo(admin.ModelAdmin):
    search_fields = ('user_created','first_name','last_name','student_number','guardian_name','guardian_contact')
    list_display = ['user_created','first_name','last_name','student_number','guardian_name','guardian_contact']

class ClinicVisitors(admin.ModelAdmin):
    search_fields = ('date_and_time_of_visit','student_name','student_number','year_level_and_course')
    list_display = ['date_and_time_of_visit','student_name','student_number','year_level_and_course']

class StudentCRecord(admin.ModelAdmin):
    search_fields = ('student_record','date_and_time_of_visit','chief_complaints','treatments','remarks')
    list_display = ['student_record','date_and_time_of_visit','chief_complaints','treatments','remarks']

admin.site.register(Student, StudentInfo)
admin.site.register(DailyClinicRecords, ClinicVisitors)
admin.site.register(StudentClinicRecords, StudentCRecord)
