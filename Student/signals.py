from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from Admin.models import StudentProfile
from .models import StudentRegistration










@receiver(post_save, sender= StudentProfile)  
def updateStudentProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.full_name = profile.name
        user.email = profile.email
        user.address = profile.address
        user.phone   =  profile.phone
        user.mobile  =  profile.mobile 
        user.save( ) 




@receiver(post_save, sender= StudentRegistration)  
def updateStudentProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.name = profile.name
        user.email = profile.email
        user.address = profile.address
        user.mobile  =  profile.mobile 
        user.save( ) 




@receiver(post_delete,sender=StudentRegistration)
def deleteStudent(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()













