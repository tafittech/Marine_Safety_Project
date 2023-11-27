from django.contrib import admin


from .models import (
    Message, AdminMessage
) 

# Register your models here.
admin.site.register(AdminMessage)
admin.site.register(Message)
