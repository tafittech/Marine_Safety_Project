from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login, logout, authenticate, 
)

from  .models import StudentUser, StudentProfile
from .forms import(
     StudentRegisterForm, StudentUpdateForm, 
     StaffRegisterForm,
)


# Create your views here

def loginStudent(request):
    page = 'student-login'

    if request.user.is_authenticated:
        return redirect('student-user') 

    if request.method ==  'POST':
        email = request.POST['email']
        password = request.POST['password']        
        try:
            user = StudentUser.objects.get(email=email)
        except:
            messages.error(request,'email does not exist')
        
        user =authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student')
        else:
            messages.error(request,'Username OR password is incorrect')

    return render(request, 'student_login.html')


def logoutStudent(request):
    logout(request)
    return redirect('home')

def studentRegister(request):
    page  ='student-register'
    form  = StudentRegisterForm()
    form2 = StaffRegisterForm()
    if request.method == 'POST':
        form  =  StudentRegisterForm(request.POST)
        form2 =  StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            messages.success(request, 'Student acount was created!')
            login(request, user)
            return redirect('student-account')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'student_login.html',{'page':page,'form':form, 'form2':form2} )

def staffTrainingRegister(request):
    page  ='student-register'
    form = StaffRegisterForm()
    if request.method == 'POST':
        form =  StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            messages.success(request, 'Student acount was created!')
            login(request, user)
            return redirect('student-account')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'student_login.html',{'page':page,'form':form} )

@login_required(login_url='student-login')
def studentProfile(request):
    profiles = StudentProfile.objects.all() 
    return render(request, 'student.html', {'account':profiles })

def studentDetail(request, pk):
    student = StudentProfile.objects.get(id=pk)
    return render(request, 'student-details.html', {'user':student })


def studentAccount(request):
    studentAccount = request.user.studentuser.studentprofile
    return render(request, 'student-account.html', {'user':studentAccount})


def editStudentAccount(request):
    profile = request.user.studentuser.studentprofile
    form     = StudentUpdateForm(instance=profile)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save() 
            return redirect('student-account')


    return render(request,'edit-student-account.html',{'edit2':form, 'user':profile})






