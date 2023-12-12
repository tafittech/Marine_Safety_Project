from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect

from .models import (
    Course
)

# Create your views here.

def addCourse(request):
    course = ad
    return render(request, 'add_course.html',{})

def addCourseSave(request):
   pass
           
               
