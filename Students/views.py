from django.shortcuts import render

# Create your views here
def studentProfile(request):
    return render(request, 'student-file.html', {})