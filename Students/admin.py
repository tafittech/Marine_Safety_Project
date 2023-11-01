from django.contrib import admin



from .models import StudentEmergencyProfile, StudentProfile, StudentUser
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(StudentProfile)
admin.site.register(StudentEmergencyProfile)
