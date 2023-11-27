from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from Students.models import StudentProfile
from Admin.models import AdminProfile

from .forms import Message_Form, AdminMessageForm


# Create your views here.


@login_required(login_url='student-login')
def messageCenter(request):
    profile = request.user.studentuser.studentprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context ={ 
        'messageRequest':messageRequest, 'unreadCount':unreadCount
    }
    return render(request, 'messageCenter.html', context)


def viewMessage(request, pk):
    page = 'message'
    profile = request.user.studentuser.studentprofile
    message = profile.messages.get(id=pk)
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    if message.is_read == False:
        message.is_read = True
        message.save()
    context ={'message':message, 'unreadCount':unreadCount}
    return render(request, 'viewMessage.html',context )




def createMessage(request, pk):
    recipient = StudentProfile.objects.get(id=pk)
    form  = Message_Form()
    profile = request.user.studentuser.studentprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    
    try:
        sender = request.user.studentuser.studentprofile
    except:
        sender = None

    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name  = sender.first_name + "  " + sender.last_name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('message')
    context={
        'recipient':recipient,'unreadCount':unreadCount,
        'form':form,
    }
    return render(request, 'createMessage.html', context)


def deleteMessage(request, pk):
    profile = request.user.studentuser.studentprofile
    message = profile.messages.filter(id=pk)
    
    if request.method == 'POST':
        message.delete()
        redirect('message')

    context ={'message':message}
    return render(request, 'deleteMessage.html',context )



#admin message-center view here.

def adminMessageCenter(request):
    page ='admin-message'
    profile = request.user.adminprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context ={ 
        'messageRequest':messageRequest, 'unreadCount':unreadCount
    }
    return render(request, 'message-Center.html', context)



def viewAdminMessage(request, pk):
    page = 'message'
    profile = request.user.adminprofile
    message = profile.messages.get(id=pk)
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    if message.is_read == False:
        message.is_read = True
        message.save()
    context ={'message':message, 'unreadCount':unreadCount}
    return render(request, 'view-Message.html',context )



def createAdminMessage(request, pk):
    recipient = AdminProfile.objects.get(id=pk)
    form  = AdminMessageForm()
    profile = request.user.adminprofile
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    
    try:
        sender = request.user.adminprofile
    except:
        sender = None

    if request.method == 'POST':
        form = AdminMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name  = sender.first_name + "  " + sender.last_name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent!')
            return redirect('admin-message')
    context={
        'recipient':recipient,'unreadCount':unreadCount,
        'form':form,
    }
    return render(request, 'create-Message.html', context)


def deleteAdminMessage(request, pk):
    profile = request.user.adminprofile
    message = profile.messages.filter(id=pk)
    
    if request.method == 'POST':
        message.delete()
        redirect('message')

    context ={'message':message}
    return render(request, 'delete-Message.html',context )


    



