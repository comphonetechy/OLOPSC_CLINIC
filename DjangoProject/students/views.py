from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Student, DailyClinicRecords, StudentClinicRecords
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import StudentClinicRecordsForm
# Create your views here.

def homepage(request):
    data = Student.objects.all().order_by('-id')

    context = {
        'student': data
    }
    return render(request, "students/index.html", context)

def search(request):
    entry = request.GET.get('search','')
    data = Student.objects.filter(Q (student_number__icontains=entry)).order_by('-id') or Student.objects.filter(Q (last_name__icontains=entry)).order_by('-id')
    
    context = {
        'student': data
    }
    return render(request, "students/index.html", context)

def add(request):
    return render(request, "students/add.html")

def addstudentrecord(request, data_id):
  # create object of form
    form = StudentClinicRecordsForm(request.POST or None, request.FILES or None)
    student = Student.objects.all()
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context = { 'form':form, 'dataid':data_id, 'student':student}
    return render(request, "students/add_student_record.html", context)


def addvisitor(request):
    return render(request, "students/add_visitor.html")

def processadd(request):
    f_name = request.POST.get('first_name')
    l_name = request.POST.get('last_name')
    s_number = request.POST.get('student_number')
    g_name = request.POST.get('guardian_name')
    g_contact = request.POST.get('guardian_contact')
    date = request.POST.get('date')
    time = request.POST.get('time')
    user_created = str(date) + " " + str(time)
    if f_name == "":
         return render(request, 'students/add.html', {'error_message' :'empty details'})
    try:
        n = Student.objects.get(first_name=f_name)
        return render(request, 'students/add.html', {'error_message' :'dubplicated info'})
    except ObjectDoesNotExist:
        student = Student.objects.create(user_created=user_created,first_name=f_name, last_name=l_name, student_number=s_number, guardian_name=g_name, guardian_contact=g_contact)
        student.save()
        return HttpResponseRedirect('/')

def processaddvisitor(request):
    date = request.POST.get('date')
    time = request.POST.get('time')
    date_time = str(date) + " " + str(time)
    studname = request.POST.get('s_name')
    studnum = request.POST.get('s_number')
    year = request.POST.get('year_level')
    course = request.POST.get('course')
    yearcourse = year + " " + course
    if studname == "":
         return render(request, 'students/add_visitor.html', {'error_message' :'error details'})
    record = DailyClinicRecords.objects.create(date_and_time_of_visit=date_time, student_name=studname, student_number=studnum, year_level_and_course=yearcourse)
    record.save()
    return HttpResponseRedirect('/')

def detail(request, student_id):
    student_clinic_record = StudentClinicRecords.objects.all()
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("profile does not exist")
    return render(request, "students/student_detail.html", {'student':student, 'data':student_clinic_record,})


def delete(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return HttpResponseRedirect('/')


def edit(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("profile does not exist")
    return render(request, "students/edit.html", {'student':student})



def processedit(request, student_id):
    stud_id = get_object_or_404(Student, pk=student_id)
    try:
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        s_number = request.POST.get('student_number')
        g_name = request.POST.get('guardian_name')
        g_contact = request.POST.get('guardian_contact')
    except (KeyError, Student.DoesNotExist):
        return render(request, 'students/details.html', {'user':stud_id,'error_message': "Problem updating record"})
    else:
        stud_profile = Student.objects.get(id=student_id)
        stud_profile.first_name = f_name
        stud_profile.last_name = l_name
        stud_profile.student_number = s_number
        stud_profile.guardian_name = g_name
        stud_profile.guardian_contact = g_contact
        stud_profile.save()
        return HttpResponseRedirect(reverse('students:detail', args=(student_id,)))

def dailyclinicrecords(request):
    data = StudentClinicRecords.objects.all().order_by('-id')
    context = {
        'record': data
    }
    return render(request, "students/dailyclinicrecords.html", context)