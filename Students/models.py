from django.db import models
from django.contrib.auth.models import (
      BaseUserManager
)

from Admin.models import User



# Create your models here

class StudentUser(User):
    class Role(models.TextChoices ):
        STUDENT   = 'STUDENT','student'
        STAFF     = 'STAFF','staff'

    base_role = Role.STUDENT

    role = models.CharField(max_length=255 , choices=Role.choices) 

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
        


class StudentManger(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=StudentUser.Role.STUDENT)
    
class Student(StudentUser):

    base_role = StudentUser.Role.STUDENT

    student = StudentManger()
    
    class Meta:
        proxy = True


class StaffStudentManger(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=StudentUser.Role.STAFF)
    
class StaffStudent(StudentUser):

    base_role = StudentUser.Role.STAFF

    staff = StaffStudentManger()
    
    class Meta:
        proxy = True

class StudentProfile(models.Model):
    GENDER_TYPE  ={('MALE','male'),('FEMALE','female')}
    STUDENT_TYPE ={('FOREIGNER','foreigner'),('LOCAL','local')}

    user              = models.OneToOneField(StudentUser,on_delete=models.CASCADE, null=True , blank=True)
    email             = models.EmailField(max_length=255, blank = True, null=True)
    name              = models.CharField(max_length=255, blank = True, null=True)
    profile_image      = models.ImageField(blank=True, null=True, default= 'default1.jpeg')
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


    def __str__(self):
        return str(self.user)




class StudentEmergencyProfile(models.Model):

    emergency_name =models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, blank = True, null=True)
    relationship = models.CharField(max_length=255, blank = True, null=True)
    emergency_address = models.CharField(max_length=255, blank = True, null=True)
    emergency_phone   = models.CharField(max_length=255, blank = True, null=True)


    def __str__(self):
        return self.emergency_name