from django.urls import path


from .views import (
    home, register, loginUser,
    logoutUser, profile,staff
)


urlpatterns = [
    path('', home, name= 'dashboard'),
    path('login/', loginUser , name= 'login'),
    path('register/', register , name= 'register'),
    path('logout/', logoutUser , name= 'logout'),
    path('account/', profile , name= 'account'),
    path('account/<str:pk>/', staff , name= 'staff'),
]