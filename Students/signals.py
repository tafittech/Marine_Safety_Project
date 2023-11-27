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
            first_name = user.first_name,
            last_name  = user.last_name 
        )
       



@receiver(post_save,sender=Student)
def createStaff(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = StudentProfile.objects.create(
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
        user.email  =  profile.email
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.address = profile.address
        user.occupation   =  profile.occupation
        user.gender   =  profile.gender
        user.date_of_birth   =  profile.date_of_birth
        user.phone   =  profile.phone
        user.mobile  =  profile.mobile
        user.student_type = profile.student_type
        user.nationality   =  profile.nationality
        user.national_id   =  profile.national_id
        user.birth_cert_number   =  profile.birth_cert_number
        user.employer   =  profile.employer
        user.employer_phone   =  profile.employer_phone
        user.save( )


@receiver(post_delete,sender=StudentProfile)
def deleteStaff(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()