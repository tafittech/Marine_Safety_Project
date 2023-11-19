from django.urls import path


from .views import (
    studentAccount, studentRegister
)


urlpatterns = [
    
    path('student-register/', studentRegister, name='student-register'), 
    path('student-account/', studentAccount , name= 'student-account'),
    
]