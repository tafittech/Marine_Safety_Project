from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import AdminProfile, StaffProfile

User = get_user_model()


@receiver(post_save,sender=User)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        if instance.user_type == 1:
            admin_id    = instance
            profile = AdminProfile.objects.create(
                admin_id = admin_id,      
                email = admin_id.email,
                name  = admin_id.full_name 
        )
        if instance.user_type == 2:
            admin_id    = instance
            profile = AdminProfile.objects.create(
                admin_id = admin_id,      
                email = admin_id.email,
                name  = admin_id.full_name 
        ) 



@receiver(post_save, sender= AdminProfile)  
def updateProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    admin_id    = profile.admin_id
    if created == False:
        admin_id.full_name = profile.name
        admin_id.email = profile.email
        admin_id.address = profile.address
        admin_id.phone   =  profile.phone
        admin_id.mobile  =  profile.mobile
        admin_id.staff_info = profile.staff_info
        admin_id.save( )


@receiver(post_save, sender= StaffProfile)  
def updateProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    admin_id    = profile.admin_id
    if created == False:
        admin_id.full_name = profile.name
        admin_id.email = profile.email
        admin_id.address = profile.address
        admin_id.phone   =  profile.phone
        admin_id.mobile  =  profile.mobile
        admin_id.staff_info = profile.staff_info
        admin_id.save( )


@receiver(post_delete,sender=AdminProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    admin_id = instance.admin_id 
    admin_id.delete()


@receiver(post_delete,sender=StaffProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    admin_id = instance.admin_id
    admin_id.delete()