from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login, logout, authenticate, get_user_model
) 

from .forms import StudentRegisterForm, StudentUser


# Create your views here.
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
            return redirect('account')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page,'form2':form} )

@login_required(login_url='login')
def studentAccount(request):
    account = request.user.studentuser
    studentAccount = account.studentprofile
    context = {
         'user2':studentAccount, 'user':account
    }
    return render(request, 'user-account.html', context)