from django.contrib.auth import get_user_model
from django.forms  import ModelForm
from django   import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms  import (
    ReadOnlyPasswordHashField
)

from Admin.models import StudentProfile
from .models import StudentRegistration




class StudentUpdateForm(ModelForm):

    class Meta:
        model  = StudentProfile
        fields =[
            'name', 'profile_image','email',
            'address','phone','mobile',
        ] 
        

        def __init__(self, *args,**kwargs):
            super(StudentUpdateForm, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-group-text'})



class StudentRegistrationForm(ModelForm):

    class Meta:
        model  = StudentRegistration
        fields =[
            'first_name','last_name', 'profile_image','address',
            'occupation', 'gender','date_of_birth','phone','mobile','student_type','nationality', 'national_id','birth_cert_number','email','employer', 'employer_phone'
        ]
        

        def __init__(self, *args,**kwargs):
            super(StudentRegistrationForm, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-group-text'})


