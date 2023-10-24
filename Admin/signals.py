from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import AdminProfile

User = get_user_model()


@receiver(post_save,sender=User)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = AdminProfile.objects.create(
            user = user,      
            email = user.email,
            name  = user.full_name 
        )
        print('profile created' )


@receiver(post_delete,sender=AdminProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()