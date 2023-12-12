from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from Students.forms import StudentCourseInfoForm
from .models import (
    Course
)
from .forms import (
    addCourse_Form
)

# Create your views here.

def addCourse(request):
    course = addCourse_Form()
    if request.method == 'POST':
        addCourse = addCourse_Form(request.POST)
        try:
            addCourse.save()
            messages.success(request,"Successfully add a course")
            return redirect('course')
        except:
            messages.error(request, "Failure to add course")
            return redirect('course')     

    return render(request, 'add_course.html',{'form':course})



def courseRegistration(request):
    st_user = request.user.studentuser.studentprofile
    reg_form= StudentCourseInfoForm()
    if request.method == 'POST':
        reg_student = StudentCourseInfoForm(request.POST, request.FILES,instance=st_user )
        try:
            reg_student.save()
            messages.success(request,"Successfully Registered Student")
            return redirect('student-account')
        except:
            messages.error(request, "Failure to Register Student")
            return redirect('course-register')
    context ={
        'user':st_user, 'form':reg_form,
    }
    return render ( request, 'CourseRegistration.html', context) 
               
