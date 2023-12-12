from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import (
    Course
)
from .forms import (
    addCourse_Form
)

# Create your views here.

def addCourse(request):
    course = addCourse_Form()
    return render(request, 'add_course.html',{'form':course})

def addCourseSave(request):
   pass
           
               
