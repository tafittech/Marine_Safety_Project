from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



# ---app models--
from .models import StudentProfile
from Admin.models import User

@receiver(post_save,sender=User)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        if instance.student == True:
            user    = instance
            StudentProfile.objects.create(
                user = user,      
                email = user.email,
                first_name = user.first_name,
                last_name  = user.last_name 
        )
       

       
@receiver(post_save, sender= StudentProfile)  
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
        user.student_type = profile.student_type
        user.save( )





@receiver(post_delete,sender=StudentProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()