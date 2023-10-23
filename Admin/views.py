from django.shortcuts import render

# Create your views here.
def adminDashBoard(request):
    return render(request, 'admin_dash_board.html', {})