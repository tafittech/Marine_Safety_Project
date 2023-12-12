from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from Students.forms import StudentUpdateForm
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
    reg_form= StudentUpdateForm()
    context ={
        'user':st_user, 'form':reg_form,
    }
    return render ( request, 'CourseRegistration.html', context) 
               
