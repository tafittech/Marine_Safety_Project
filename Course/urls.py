from django.urls import path

from .views import (
    addCourse, addCourseSave
)



urlpatterns=[
    path('course/', addCourse, name= 'course'),
    path('add-course/', addCourseSave, name= 'add-course'),
]