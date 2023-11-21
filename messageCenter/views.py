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







    



