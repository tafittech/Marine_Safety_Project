from django.urls import path




from .views import (
    studentProfile, studentUserAccount, editStudentAccount,
    student, studentRegister 

) 




urlpatterns = [   
    path('student-account/', studentUserAccount , name='student-user'),
    path('edit-student-account/', editStudentAccount, name='edit-student'),
    path('student-registration/', studentRegister, name= 'registration'), 
    path('student-profiles/', studentProfile, name= 'student-account'),
    path('student-profiles/<str:pk>/', student, name= 'student'), 
]