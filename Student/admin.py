from django.contrib import admin

# import your models here.
from .models import StudentUser, StudentProfile

# Register your models here.
admin.site.register(StudentUser)
admin.site.register(StudentProfile)