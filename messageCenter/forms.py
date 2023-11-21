from django.forms  import ModelForm
from django   import forms

from .models  import Message, AdminMessage


class Message_Form(ModelForm):
    class Meta:
        model = Message
        fields= [
            'name', 'email', 
            'subject', 'body',
        ]
        labels = {
            'name':'Full Name', 'email':'Email', 
            'subject':'Subject', 'body':'Message',
        }
    
    def __init__(self, *args,**kwargs):
            super(Message_Form, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-text'})


class AdminMessageForm(ModelForm):
    class Meta:
        model = AdminMessage
        fields= [
            'name', 'email', 
            'subject', 'body',
        ]
        labels = {
            'name':'Full Name', 'email':'Email', 
            'subject':'Subject', 'body':'Message',
        }
    
    def __init__(self, *args,**kwargs):
            super(AdminMessageForm, self).__init__(*args,*kwargs)

            for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input-text'})