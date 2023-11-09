from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import AdminProfile,StudentProfile

User = get_user_model()

@receiver(post_save,sender=User)
def createStudent(sender, instance, created,*args, **kwargs):
    if created and sender.student:
        user    = instance
        profile = StudentProfile.objects.create(
            user = user,      
            email = user.email,
            first_name = user.first_name,
            last_name  = user.last_name  
        )


@receiver(post_save,sender=User)
def createStaff(sender, instance, created,*args, **kwargs):
    if created and not sender.student:
        user    = instance
        profile = AdminProfile.objects.create(
            user = user,      
            email = user.email,
            first_name = user.first_name,
            last_name  = user.last_name 
        )
        


@receiver(post_save, sender= AdminProfile)  
def updateProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.address = profile.address
        user.phone   =  profile.phone
        user.mobile  =  profile.mobile
        user.staff_info = profile.staff_info
        user.save( )

          
@receiver(post_save, sender= StudentProfile)  
def updateStudentProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.first_name        = profile.first_name
        user.last_name         = profile.last_name
        user.address           = profile.address
        user.occupation        = user.occupation 
        user.gender            = user.gender 
        user.date_of_birth     = user.date_of_birth 
        user.phone             = profile.phone
        user.mobile            = profile.mobile
        user.student_type      = user.student_type 
        user.nationality       = user.nationality
        user.national_id       = user.national_id
        user.birth_cert_number = user.birth_cert_number 
        user.email             = user.email
        user.employer          = user.employer 
        user.employer_phone    = user.employer_phone 
        user.save( )

@receiver(post_delete,sender=AdminProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()


@receiver(post_delete,sender=StudentProfile)
def deleteStudent(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()