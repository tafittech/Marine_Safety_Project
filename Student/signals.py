from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model


from .models import StudentUser, StudentProfile


@receiver(post_save,sender=StudentUser)
def createStudent(sender, instance, created,*args, **kwargs):
    if created:
        user    = instance
        profile = StudentProfile.objects.create(
            user = user,      
            email = user.email,
            first_name = user.first_name,
            last_name  = user.last_name 
        )

@receiver(post_save, sender=StudentProfile)  
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

@receiver(post_delete,sender=StudentProfile)
def deleteStudent(sender,instance,*args, **kwargs):
    user = instance.user 
    user.delete()