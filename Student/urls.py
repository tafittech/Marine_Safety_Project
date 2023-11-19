from django.urls import path


from .views import (
    studentRegister, studentAccount,
    studentProfile, loginStudent, logoutStudent
)


urlpatterns = [
    
    path('login-student/', loginStudent , name= 'login-student'),
    path('logout-student/', logoutStudent , name= 'logout-student'),
    path('student-register/', studentRegister, name='student-register'),
    path('student/', studentProfile , name= 'student'), 
    path('student-account/', studentAccount , name= 'student-account'),
    
]