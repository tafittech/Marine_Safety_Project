from django.urls import path




from .views import studentProfile




urlpatterns = [
    path('student/', studentProfile, name= 'student')
]