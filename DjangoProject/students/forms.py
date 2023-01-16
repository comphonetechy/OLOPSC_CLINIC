# import form class from django
from django import forms
 
# import GeeksModel from models.py
from .models import StudentClinicRecords
 
# create a ModelForm
class StudentClinicRecordsForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = StudentClinicRecords
        fields = "__all__"