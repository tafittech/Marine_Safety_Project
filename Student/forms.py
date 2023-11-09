from django.forms  import ModelForm
from django   import forms
from django.contrib.auth.forms import UserCreationForm

from Admin.models import StudentProfile

class StudentRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields =[
            'email','first_name','last_name',
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
        user = super(StudentRegisterForm,self).save(commit=True   )
        user.set_password(self.cleaned_data["password1"])
        user.active =True
        user.student=True
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
        
        def __init__(self, *args,**kwargs):
            super(StudentUpdateForm, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-group-text'})