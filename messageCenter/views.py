from django.shortcuts import render

# Create your views here.

def messageCenter(request):
    return render(request, 'messageCenter.html', {})
