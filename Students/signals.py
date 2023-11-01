from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



# ---app models--
from .models import StudentProfile, Student, StaffStudent

@receiver(post_save,sender=StaffStudent)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = StudentProfile.objects.create(
            user = user,      
            email = user.email,
            name  = user.full_name 
        )
       



@receiver(post_save,sender=Student)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = StudentProfile.objects.create(
            user = user,     
            email = user.email,
            name  = user.full_name 
        )
       
@receiver(post_save, sender= StudentProfile)  
def updateProfile(sender, instance ,created, *args, **kwargs ):
    profile = instance
    user    = profile.user
    if created == False:
        user.full_name = profile.name
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