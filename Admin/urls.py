from django.urls import path


from .views import (
    home, register, loginUser,
    logoutUser, profile,staff,
    userAccount
)


urlpatterns = [
    path('', home, name= 'dashboard'),
    path('login/', loginUser , name= 'login'),
    path('logout/', logoutUser , name= 'logout'),
    path('register/', register , name= 'register'),
    path('profile/', profile , name= 'account'),
    path('profile/<str:pk>/', staff , name= 'staff'),
    path('account/', userAccount , name= 'user'),
]