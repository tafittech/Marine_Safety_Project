from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



# ---app models--
from .models import StudentProfile, StudentUser



@receiver(post_save,sender=StudentUser)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = StudentProfile.objects.create(
            user = user,      
            email = user.email,
            surname  = user.last_name 
        )
        print('profile created' )





@receiver(post_delete,sender=StudentProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()