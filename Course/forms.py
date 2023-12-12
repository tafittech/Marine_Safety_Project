from django.forms  import ModelForm
from django   import forms


from .models import (
    Course
)

class addCourse_Form(ModelForm):

    class Meta:
        model= Course
        fields = [ 'course_name']
        labels = {
            'course_name':'Course Name'
        }
    
    def __init__(self, *args,**kwargs):
        super(addCourse_Form, self).__init__(*args,*kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-group-text'})