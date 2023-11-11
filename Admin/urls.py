from django.urls import path

from Student.views import studentRegister
from .views import (
    dashBoard, register, loginUser,
    logoutUser, profile,staff, inbox,
    userAccount, editAccount, viewMessage,
    createMessage
)


urlpatterns = [
    path('dashboard/', dashBoard, name= 'dashboard'),
    path('login/', loginUser , name= 'login'),
    path('logout/', logoutUser , name= 'logout'),
    path('register/', register , name= 'register'), 
    path('edit-account/', editAccount , name= 'edit'),
    path('profile/', profile , name= 'account'),
    path('profile/<str:pk>/', staff , name= 'staff'),
    path('account/', userAccount , name= 'user'),
    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>', viewMessage, name='view-message'),
    path('compose-message/<str:pk>', createMessage, name= 'compose-message'),
]