from django.urls import path




from .views import (
    studentProfile, loginStudent, logoutStudent,
    studentRegister, studentAccount, editStudentAccount,
    studentDetail
) 




urlpatterns = [
    
    path('student-login/', loginStudent, name= 'student-login'),
    path('student-logout/', logoutStudent , name= 'student-logout'),
    path('student/', studentProfile, name= 'student'),
    path('student/<str:pk>/', studentDetail , name= 'student-details'), 
    path('student-register/', studentRegister , name= 'student-register'),
    path('student-account/', studentAccount , name= 'student-account'),
    path('edit-student-account/', editStudentAccount , name= 'edit-student-account'),
    
]