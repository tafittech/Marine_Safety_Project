from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import (
    login, logout, authenticate, get_user_model
) 


from .models import AdminProfile, Message
from .forms  import RegisterForm, adminUpdateForm, Message_Form 

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
    return redirect('home')

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
            return redirect('edit')
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


#---Message Center View Start here.

@login_required(login_url='login')
def inbox(request):
    profile = request.user.adminprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context ={ 
        'messageRequest':messageRequest, 'unreadCount':unreadCount
    }
    return render(request, 'inbox.html', context)


def viewMessage(request, pk):
    page = 'inbox'
    profile = request.user.adminprofile
    message = profile.messages.get(id=pk)
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    if message.is_read == False:
        message.is_read = True
        message.save()
    context ={'message':message, 'unreadCount':unreadCount}
    return render(request, 'view-inbox.html',context )

def createMessage(request, pk):
    recipient = AdminProfile.objects.get(id=pk)
    form  = Message_Form()
    profile = request.user.adminprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    
    try:
        sender = request.user.adminprofile
    except:
        sender = None

    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name  = sender.first_name + " " + sender.last_name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('staff', pk=recipient.id)
        
    context={
        'recipient':recipient,'unreadCount':unreadCount,
        'form':form,
    }
    return render(request, 'compose-message.html', context)


def deleteMessage(request, pk):
    
    message = Message.objects.get(id=pk)
    
    if request.method == 'POST':
        message.delete()
        redirect('inbox')

    context ={'message':message}
    return render(request, 'delete-message.html',context )


#--- Student Views created here.

def studentRegister(request):
    page = 'student-register'
    #form =  StudentRegisterForm()
    #if request.method ==  'POST':
        #form =  StudentRegisterForm(request.POST)
        #if form.is_valid():
        #    user = form.save(commit=False)
        #    user.email = user.email,
        #    user.first_name = user.first_name,
        #    user.last_name  = user.last_name, 
        #    user.save()
        #    messages.success(request, 'User acount was created!')
        #    login(request, user)
        #    return redirect('account')
        #else:
        #    messages.warning(request, 'An error has occurred during registration')
    return render(request, 'login_register.html',{'page':page} )