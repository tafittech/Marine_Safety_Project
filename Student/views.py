from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login, logout, authenticate, get_user_model
) 

from . models import (
    StudentProfile, StudentUser
)
from .forms import (
    StudentRegisterForm
)


# Create your views here.
def loginStudent(request):
    page = 'login-student'

    if request.user.is_authenticated:
        return redirect('student') 

    if request.method ==  'POST':
        email = request.POST['email']
        password = request.POST['password']        
        try:
            user = StudentProfile.objects.get(email=email)
        except:
            messages.error(request,'email does not exist')
        
        user =authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student')
        else:
            messages.error(request,'Username OR password is incorrect')

    return render(request, 'login_student.html')

def logoutStudent(request):
    logout(request)
    return redirect('home')

def studentRegister(request):
    page = 'student-register'
    form =  StudentRegisterForm()
    if request.method ==  'POST':
        form =  StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email,
            user.first_name = user.first_name,
            user.last_name  = user.last_name, 
            user.save()
            messages.success(request, 'User acount was created!')
            login(request, user)
            return redirect('student')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page,'form2':form} )

@login_required(login_url='login-student')
def studentProfile(request):
    profiles = StudentProfile.objects.all() 
    return render(request, 'students.html', {'account2':profiles })



def studentAccount(request):
    studentAccount= request.studentprofile
    context = {
         'user2':studentAccount,
    }
    return render(request, 'student-account.html', context)