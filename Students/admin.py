from django.contrib import admin



from .models import StudentEmergencyProfile, StudentProfile
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(StudentEmergencyProfile)
