from django.contrib import admin



from .models import StudentEmergencyInfo, StudentProfile
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(StudentEmergencyInfo)
