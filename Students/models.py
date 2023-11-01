from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser, AbstractUser,BaseUserManager
)



# Create your models here

class StudentUser(AbstractUser):
    class StudentType(models.TextChoices ):
        FOREIGNER = 'FOREIGNER','foreigner'
        LOCAL     = 'LOCAL','local'

    base_student_type = StudentType.LOCAL

    student_type = models.CharField(max_length=255 , choices= StudentType.choices) 

    def save(self, *args, **kwargs):
        if not self.pk:
            self.student_type = self.base_student_type
            return super().save(*args, **kwargs)


class StudentProfile(models.Model):
    GENDER_TYPE ={
        ('MALE','male'),
        ('FEMALE','female')
    }
    email              = models.EmailField(max_length=255, blank = True, null=True)
    surname            = models.CharField(max_length=255, blank = True, null=True)
    first_name         = models.CharField(max_length=255, blank = True, null=True)
    image_photo        = models.ImageField(blank=True, null=True, default= 'default1.jpeg')
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
        return self.surname




class StudentEmergencyProfile(models.Model):

    emergency_name =models.ForeignKey(StudentProfile, on_delete=models.DO_NOTHING, blank = True, null=True)
    relationship = models.CharField(max_length=255, blank = True, null=True)
    emergency_address = models.CharField(max_length=255, blank = True, null=True)
    emergency_phone   = models.CharField(max_length=255, blank = True, null=True)


    def __str__(self):
        return self.emergency_name