from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login, logout, authenticate, get_user_model
) 


from .models import AdminProfile
from .forms  import RegisterForm, adminUpdateForm 

User = get_user_model()

@login_required(login_url='login')
def dashBoard(request): 
    return render(request, 'admin_dash_board.html',{})

# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('account') 

    if request.method ==  'POST':
        email = request.POST['email']
        password = request.POST['password']        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'email does not exist')
        
        user =authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request,'Username OR password is incorrect')

    return render(request, 'login_register.html')


def logoutUser(request):
    logout(request)
    return redirect('dashboard')

def register(request):
    page = 'register'
    form =  RegisterForm()
    if request.method ==  'POST':
        form =  RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email
            user.save()
            messages.success(request, 'User acount was created!')
            login(request, user)
            return redirect('users')
        else:
            messages.warning(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page,'form':form} )





def profile(request):
    profiles = AdminProfile.objects.all() 
    return render(request, 'profiles.html', {'account':profiles })


def staff(request, pk):
    staff = AdminProfile.objects.get(id=pk)
    return render(request, 'user-profiles.html', {'user':staff })


@login_required(login_url='login')
def userAccount(request):
    user_account = request.user.adminprofile
    return render(request, 'user-account.html', {'user':user_account})


def editAccount(request):
    profile  = request.user.adminprofile
    form     = adminUpdateForm(instance=profile)

    if request.method == 'POST':
        form = adminUpdateForm(request.POST, request.FILES ,  instance=profile)
        if form.is_valid():
            form.save()
            
            return redirect('user')


    return render(request,'edit-account.html',{'edit2':form, 'user':profile})