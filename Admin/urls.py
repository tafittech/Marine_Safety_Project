from django.urls import path


from .views import adminDashBoard

urlpatterns = [
    path('', adminDashBoard, name= 'dashboard'),
]