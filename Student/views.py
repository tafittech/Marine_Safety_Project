from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import (
    login,
) 


#imports for view here.
from Admin.models import StudentProfile
from .forms  import StudentRegisterForm
from .forms import StudentUpdateForm

# Create your views here.
@login_required( login_url='login')
def studentProfile(request):
    profiles = StudentProfile.objects.all() 
    return render(request, 'student-profiles.html', {'account':profiles })

def student(request, pk):
    student = StudentProfile.objects.get(id=pk)
    return render(request, 'student-user-profile.html', {'user':student })

@login_required(login_url= 'login')
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


    return render(request,'edit-student-account.html',{'edit2':form, 'user':profile})


def studentRegister(request):
    page = 'student-register'
    form =  StudentRegisterForm()
    if request.method ==  'POST':
        form =  StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            messages.success(request, 'Student acount was created!')
            login(request, user)
            return redirect('student-user')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page,'form2':form} )


