from django.urls import path




from .views import (
    studentProfile, studentUserAccount, editStudentAccount,
    student, studentRegister 

) 




urlpatterns = [   
    path('student-account/', studentUserAccount , name='student-account'),
    path('edit-student-account/', editStudentAccount, name='edit-student'),
    path('student-registration/', studentRegister,name='student-register'), 
    path('student-profiles/', studentProfile, name= 'student-profile'),
    path('student-profiles/<str:pk>/', student, name= 'student'), 
]