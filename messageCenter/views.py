from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from Admin.models import User
from .models import Message
from .forms import Message_Form


# Create your views here.


@login_required(login_url='student-login')
def messageCenter(request):
    messageRequest = Message.objects.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    context ={ 
        'messageRequest':messageRequest, 'unreadCount':unreadCount
    }
    return render(request, 'messageCenter.html', context)


def viewMessage(request, pk):
    page = 'inbox'
    message = Message.objects.get(id=pk)
    messageRequest = Message.objects.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    if message.is_read == False:
        message.is_read = True
        message.save()
    context ={'message':message, 'unreadCount':unreadCount}
    return render(request, 'viewMessage.html',context )


def createMessage(request, pk):
    recipient = Message.objects.get(id=pk)
    form  = Message_Form()
    messageRequest = Message.objects.all()
    unreadCount = messageRequest.filter(is_read=False).count()
    
    try:
        sender = Message.objects.filter(sender)
    except:
        sender = None

    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name  = sender.name
                message.email = sender.email
            message.save()

            message.success(request, 'Your message was successfully sent!')
            return redirect('staff', pk=recipient.id)
        
    context={
        'recipient':recipient,'unreadCount':unreadCount,
        'form':form,
    }
    return render(request, 'createMessage.html', context)


def deleteMessage(request, pk):
    
    message = Message.objects.filter(id=pk)
    
    if request.method == 'POST':
        message.delete()
        redirect('home')

    context ={'message':message}
    return render(request, 'deleteMessage.html',context )







    



