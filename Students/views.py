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

def loginStudentUser(request):
    page = 'student-login'

    if request.user.is_authenticated:
        return redirect('account') 

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
            return redirect('student-account')
        else:
            messages.error(request,'Username OR password is incorrect')

    return render(request, 'student_login_register.html')


def logoutStudentUser(request):
    logout(request)
    return redirect('home')

def studentRegister(request):
    page  ='student-register'
    form  = StudentRegisterForm()
    form2 = StaffRegisterForm()
    if request.method == 'POST':
        form  =  StudentRegisterForm(request.POST)
        form2 =  StaffRegisterForm(request.POST)
        if form.is_valid() or form2.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            messages.success(request, 'Student acount was created!')
            login(request, user)
            return redirect('edit-student')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'student_login_register.html',{'page':page,'form':form, 'form2':form2} )

@login_required(login_url='student-login')
def studentProfile(request):
    profiles = StudentProfile.objects.all() 
    return render(request, 'student-profiles.html', {'account':profiles })

def student(request, pk):
    staff = StudentProfile.objects.get(id=pk)
    return render(request, 'student-user-profiles.html', {'user':staff })


def studentUserAccount(request):
    user_account = request.user.studentprofile
    return render(request, 'student-user-account.html', {'user':user_account})


def editStudentAccount(request):
    profile  = request.user.studentprofile
    form     = StudentUpdateForm(instance=profile)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, request.FILES ,  instance=profile)
        if form.is_valid():
            form.save()
            
            return redirect('student-user')


    return render(request,'edit-account.html',{'edit2':form, 'user':profile})






