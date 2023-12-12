from django.urls import path

from .views import (
    addCourse,courseRegistration
)



urlpatterns=[
    path('course/', addCourse, name= 'course'),
    path('course/register/', courseRegistration, name='course-register')
    
]