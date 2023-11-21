from django.urls import path

from .views import (
    messageCenter, viewMessage
)


urlpatterns =[
    path('message-center/', messageCenter, name='message'),
    path('message-center/<str:pk>', viewMessage, name='read-message')
]