from django.urls import path

from Student.views import studentRegister
from .views import (
    dashBoard, register, loginUser,
    logoutUser, profile,staff,
    userAccount, editAccount,
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
]