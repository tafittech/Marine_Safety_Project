from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from Admin.models import StudentProfile




@receiver(post_save, sender= StudentProfile)  
def updateStudentProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.address = profile.address
        user.phone   =  profile.phone
        user.mobile  =  profile.mobile 
        user.save( ) 