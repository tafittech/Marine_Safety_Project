from django.urls import path


from .views import (
    dashBoard, register, loginUser,
    logoutUser, profile,staff, inbox, studentAccount,
    userAccount, editAccount, viewMessage,
    createMessage, deleteMessage, studentRegister
)


urlpatterns = [
    path('', dashBoard, name= 'home'),
    path('login/', loginUser , name= 'login'),
    path('logout/', logoutUser , name= 'logout'),
    path('register/', register , name= 'register'),
    path('student-register/', studentRegister, name='student-register'), 
    path('edit-account/', editAccount , name= 'edit'),
    path('profile/', profile , name= 'account'),
    path('profile/<str:pk>/', staff , name= 'staff'),
    path('account/', userAccount , name= 'user'),
    path('student-account/', studentAccount , name= 'student-account'),
    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>', viewMessage, name='view-message'),
    path('delete-message/<str:pk>', deleteMessage, name='delete-message'),
    path('compose-message/<str:pk>', createMessage, name= 'compose-message'),
]