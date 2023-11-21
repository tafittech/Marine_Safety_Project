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







    



