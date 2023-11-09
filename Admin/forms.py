from django.contrib.auth import get_user_model
from django.forms  import ModelForm
from django   import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms  import (
    ReadOnlyPasswordHashField
)


from .models import AdminProfile


User = get_user_model()


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields =[
            'email','first_name','last_name',
            'password1', 'password2',
        ]
    
    def __init__(self, *args,**kwargs):
        super(RegisterForm, self).__init__(*args,*kwargs)

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
        user = super(RegisterForm,self).save(commit=True    )
        user.set_password(self.cleaned_data["password1"])
        user.active =True
        user.staff=True
        if commit:
            user.save()
        return user

class AdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model  = User
        fields =[
            'email','first_name','last_name',
            'password1', 'password2',
        ]
        

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords dont match')
        return password2

    def save(self, commit=True):
        # save the provided password in hashed format
        user = super(AdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    # A form for updating users. Includes all the fields on the user,
    # replaces the password field with admin's password hash display field.
    password=ReadOnlyPasswordHashField()

    class Meta:
        model  = User
        fields =[
            'email','first_name','last_name',
            'password', 'active', 'admin',
        ]

        def clean_password(self):
        #Regardless of what the user provides , return the initial value.
        #This is done here, rather than on the field, because the
        #field does not have access to the initial value
            return self.initial['password']


class adminUpdateForm(ModelForm):

    class Meta:
        model  = AdminProfile
        fields =[
            'first_name','last_name','profile_image','email','address','phone','mobile','staff_info','bio_info'
        ]
       

        def __init__(self, *args,**kwargs):
            super(adminUpdateForm, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-group-text'})