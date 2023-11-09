from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin  import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, AdminCreationForm
from .models import (
    AdminProfile
    
)

User = get_user_model()

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # the forms to add and change user instance
    form = UserAdminChangeForm #update view
    add_form = AdminCreationForm #create view

    # The fields to be used in displaying the user model.
    #These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display =('email', 'admin')
    list_filter  = ('admin','staff', 'student', 'active')
    fieldsets    =(
        (None,{'fields':('email','password',)}),
        ('Personal Info',{'fields':('first_name', 'last_name')}),
        ('Permissions',{'fields':('admin','staff','student', 'active',)}),
    )

    #add_fieldsets is not a standard  ModelAdmin attribute
    #overrides get_fieldsets to use the attribute when creating a user
    add_fieldsets =(
        (None,{
            'classes':('wide',),
            'fields':('email', 'password1', 'password2',)}
        ),
    )
    search_fields     =('email','first_name','last_name')
    ordering          =('email',)
    filter_horizontal =()

admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = AdminProfile

admin.site.register(AdminProfile, ProfileAdmin)
