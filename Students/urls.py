from django.urls import path




from .views import (
    studentProfile, loginStudentUser, logoutStudentUser,
    studentRegister, studentUserAccount, editStudentAccount,
    student
) 




urlpatterns = [
    path('student/', studentProfile, name= 'student'),
    path('student-login/', loginStudentUser, name= 'student-login'),
    path('student-logout/', logoutStudentUser , name= 'student-logout'),
    path('student-register/', studentRegister , name= 'student-register'),
    path('student-account/', studentUserAccount , name= 'student-user'),
    path('edit-student-account/', editStudentAccount , name= 'edit-student'),
    path('student-profile/', studentProfile , name= 'student-account'),
    path('student-profile/<str:pk>/', student , name= 'student'),
]