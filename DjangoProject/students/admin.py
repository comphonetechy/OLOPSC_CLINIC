from django.contrib import admin
from .models import Student, DailyClinicRecords

# Register your models here.

admin.site.site_header = "OLOPSC CLINIC"
admin.site.site_title = "OLOPSC CLINIC"
admin.site.index_title = "Welcome to OLOPSC CLINIC!"

class StudentInfo(admin.ModelAdmin):
    list_display = ['first_name','last_name','student_number','guardian_name','guardian_contact']

admin.site.register(Student, StudentInfo)
admin.site.register(DailyClinicRecords)
