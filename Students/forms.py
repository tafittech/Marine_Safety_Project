from django.contrib.auth import get_user_model
from django.forms  import ModelForm
from django   import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms  import (
    ReadOnlyPasswordHashField
)


from .models import StudentProfile
from Admin.models import User



class StudentRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields =[
            'email','first_name', 'last_name',
            'password1', 'password2',
        ]
    
    def __init__(self, *args,**kwargs):
        super(StudentRegisterForm, self).__init__(*args,*kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input-group-text'})
            

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords dont match')
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(StudentRegisterForm,self).save(commit=True )
        user.set_password(self.cleaned_data["password1"])
        user.active =True
        user.user_type=2
        if commit:
            user.save()
        return user



class StudentUpdateForm(ModelForm):

    class Meta:
        model  = StudentProfile
        fields =[
            'first_name','last_name', 'profile_image','address',
            'occupation', 'gender','date_of_birth','phone','mobile','student_type','nationality', 'national_id','birth_cert_number','email','employer', 'employer_phone'
        ] 
        labels ={
            'first_name':'First Name','last_name':'Surname', 'profile_image':'Photo',
            'address':'Address','occupation':'Occupation', 'gender':'Gender',
            'date_of_birth':'Date of Birth','phone': 'Phone Number','mobile':'Mobile Number','student_type': 'Type of Student','nationality':'Nationality', 'national_id':'National  ID/DP/Passport ID',
            'birth_cert_number':'Birth Certificate Number','email':'Email Address',
            'employer':'Employer Name', 'employer_phone':'Employer Phone Number' 
        }

    def __init__(self, *args,**kwargs):
        super(StudentUpdateForm, self).__init__(*args,*kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input-text'})
                

        