from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractUser
)

# Create your models here.
class StudentManger(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results= super().get_queryset(*args, **kwargs)
        return results.filter(student=True)


class StudentUser(AbstractUser):
    
    student = models.BooleanField(default=True)

    students = StudentManger()

    def __str__(self):
        return self.email
    


class StudentProfile(models.Model):
    GENDER_TYPE ={
        ('MALE','male'),
        ('FEMALE','female')
    }
    user          = models.OneToOneField(StudentUser,on_delete=models.CASCADE, null=True , blank=True)
    email              = models.EmailField(max_length=255, blank = True, null=True)
    last_name          = models.CharField(max_length=255, blank = True, null=True)
    first_name         = models.CharField(max_length=255, blank = True, null=True)
    profile_image      = models.ImageField(blank=True, null=True, default= 'default1.jpeg')
    address            = models.CharField(max_length=255, blank = True, null=True)
    occupation         = models.CharField(max_length=255, blank = True, null=True)
    gender             = models.CharField(max_length=50, blank = True, null=True, choices=GENDER_TYPE, default='male')
    date_of_birth      = models.CharField(max_length=255, blank = True, null=True)
    phone              = models.CharField(max_length=255, blank = True, null=True)
    mobile             = models.CharField(max_length=255, blank = True, null=True)
    nationality        = models.CharField(max_length=255, blank = True, null=True)
    national_id        = models.CharField(max_length=255, blank = True, null=True)
    birth_cert_number  = models.CharField(max_length=255, blank = True, null=True)
    employer           = models.CharField(max_length=255, blank = True, null=True)
    employer_phone     = models.CharField(max_length=255, blank = True, null=True)


    def __str__(self):
        return self.email




class StudentEmergencyProfile(models.Model):

    emergency_name =models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, blank = True, null=True,related_name='messages')
    relationship = models.CharField(max_length=255, blank = True, null=True)
    emergency_address = models.CharField(max_length=255, blank = True, null=True)
    emergency_phone   = models.CharField(max_length=255, blank = True, null=True)


    def __str__(self):
        return self.emergency_name