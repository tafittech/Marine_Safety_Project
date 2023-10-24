from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import AdminProfile
from .forms  import RegisterForm 

User = get_user_model()

def home(request): 
    return render(request, 'admin_dash_board.html',{})

# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profile') 

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
            return redirect('profiles')
        else:
            messages.success(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page,'form':form} )





def profile(request):
    profiles = AdminProfile.objects.all() 
    return render(request, 'profiles.html', {'staff':profiles })


def staff(request, pk):
    staff = AdminProfile.objects.get(id=pk)
    return render(request, 'user-profiles.html', {'user':staff })


