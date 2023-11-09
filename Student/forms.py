from django.forms  import ModelForm

from Admin.models import StudentProfile

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