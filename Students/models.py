from django.db import models
from django.contrib.auth.models import (
      BaseUserManager
)

from Admin.models import User



# Create your models here

class StudentProfile(models.Model):
    GENDER_TYPE  ={('MALE','male'),('FEMALE','female')}
    STUDENT_TYPE ={('FOREIGNER','foreigner'),('LOCAL','local')}

    user              = models.OneToOneField(User,on_delete=models.CASCADE)
    email             = models.EmailField(max_length=255, blank = True, null=True)
    first_name        = models.CharField(max_length=255, blank = True, null=True)
    last_name         = models.CharField(max_length=255, blank = True, null=True)
    profile_image     = models.ImageField(blank=True, null=True, default= 'default1.jpeg')
    address           = models.CharField(max_length=255, blank = True, null=True)
    occupation        = models.CharField(max_length=255, blank = True, null=True)
    gender            = models.CharField(max_length=50,choices=GENDER_TYPE, default='male')
    date_of_birth     = models.DateField(auto_now_add=False, blank = True, null=True)
    phone             = models.CharField(max_length=255, blank = True, null=True)
    mobile            = models.CharField(max_length=255, blank = True, null=True)
    student_type      = models.CharField(max_length=50, choices=STUDENT_TYPE,default='local')   
    nationality       = models.CharField(max_length=255, blank = True, null=True)
    national_id       = models.CharField(max_length=255, blank = True, null=True)
    birth_cert_number = models.CharField(max_length=255, blank = True, null=True)
    employer          = models.CharField(max_length=255, blank = True, null=True)
    employer_phone    = models.CharField(max_length=255, blank = True, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)


class StudentEmergencyInfo(models.Model):

    emergency_name    =models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, blank = True, null=True)
    relationship      = models.CharField(max_length=255, blank = True, null=True)
    emergency_address = models.CharField(max_length=255, blank = True, null=True)
    emergency_phone   = models.CharField(max_length=255, blank = True, null=True)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.emergency_name