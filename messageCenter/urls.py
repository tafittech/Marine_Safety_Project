from django.urls import path

from .views import (
    createAdminMessage, createMessage, deleteAdminMessage, deleteMessage, messageCenter, 
    viewAdminMessage,viewMessage, adminMessageCenter,

)


urlpatterns =[
    path('message/', adminMessageCenter, name='admin-message'),
    path('message/<str:pk>', viewAdminMessage, name='admin-view'),
    path('message/compose/<str:pk>',createAdminMessage,name='admin-send'),
    path('message/delete/<str:pk>', deleteAdminMessage, name='admin-delete'),
    path('message-center/', messageCenter, name='message'),
    path('message-center/<str:pk>', viewMessage, name='read-message'),
    path('message-center/compose/<str:pk>', createMessage, name='send-message'),
    path('message-center/delete/<str:pk>', deleteMessage, name='delete-message')
]