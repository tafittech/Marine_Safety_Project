from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser, BaseUserManager
)

 
class UserManger(BaseUserManager):
    def create_user(
            self, email, full_name, password=None, is_active=True, 
            is_student=False, is_staff=False, is_admin=False
        ):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not full_name:
            raise ValueError("User must have a Fullname")
          
        user_obj = self.model(
            email     = self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password)
        user_obj.student   = is_student
        user_obj.staff     = is_staff  
        user_obj.admin     = is_admin  
        user_obj.active    = is_active 
        user_obj.save(using=self._db)
        return user_obj
    
    def create_studentuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_student=True

        )
        return user
    
    def create_staffuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True

        )
        return user
    
    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_student=True,
            is_staff  =True,
            is_admin  =True

        )
        return user

 
class User(AbstractBaseUser):

    email     = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active    = models.BooleanField(default=True)# can login
    student   = models.BooleanField(default=False)# user non staff or superuser
    staff     = models.BooleanField(default=False)# staff user non superuser
    admin     = models.BooleanField(default=False)#superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD  = 'email' #username
    REQUIRED_FIELDS = ['full_name'] #python manage.py createsuperuser

    objects = UserManger()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_student(self):
        return self.student
    
    @property
    def is_staff(self):
        return self.staff
    
    @property 
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
    
class AdminProfile(models.Model):
    user      = models.OneToOneField(User,on_delete=models.CASCADE, null=True , blank=True)
    name       = models.CharField(max_length=255, blank=True, null=True)
    email      = models.EmailField(max_length=255, blank=True, null=True)
    staff_info = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.email)