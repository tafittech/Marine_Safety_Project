from django.urls import path

from .views import (
    createMessage, messageCenter, viewMessage
)


urlpatterns =[
    path('message-center/', messageCenter, name='message'),
    path('message-center/<str:pk>', viewMessage, name='read-message'),
    path('message-center/compose/<str:pk>', createMessage, name='send-message')
]