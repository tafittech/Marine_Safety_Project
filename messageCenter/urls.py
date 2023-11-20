from django.urls import path

from .views import messageCenter


urlpatterns =[
    path('message-center/', messageCenter, name='message')
]