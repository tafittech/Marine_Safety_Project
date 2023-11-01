from django.db import models



# Create your models here

class StudentProfile(models.Model):
    GENDER_TYPE ={
        ('MALE','M'),
        ('FEMALE','F')
    }
    email              = models.EmailField(max_length=255, blank = True, null=True)
    surname            = models.CharField(max_length=255, blank = True, null=True)
    first_name         = models.CharField(max_length=255, blank = True, null=True)
    image_photo        = models.ImageField(blank=True, null=True, default= 'default1.jpeg')
    address            = models.CharField(max_length=255, blank = True, null=True)
    occupation         = models.CharField(max_length=255, blank = True, null=True)
    gender             = models.CharField(max_length=255, blank = True, null=True, choices=GENDER_TYPE)
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