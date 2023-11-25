from django.contrib import admin


from .models import (
    StudentEmergencyProfile, StudentProfile, 
    StudentInfo,
)


# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(StudentInfo)
admin.site.register(StudentEmergencyProfile)
