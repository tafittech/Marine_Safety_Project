from django.db import models


from Admin.models import User

# Create your models here.
class Message(models.Model):
    sender      =models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    recipient   =models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True,related_name='messages' )
    name        = models.CharField(max_length=255,blank=True , null=True)
    email       = models.EmailField(max_length=255,blank=True , null=True)
    subject     = models.CharField(max_length=255,blank=True , null=True)
    body        = models.TextField()
    is_read     = models.BooleanField(default=False, null=True)
    created     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    
    class Meta:
        ordering =['is_read','-created']