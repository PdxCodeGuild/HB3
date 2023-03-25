from django import forms
from .models import ZipcodeModel, ContactMessage

class ZipcodeForm(forms.ModelForm):
    class Meta:
        model = ZipcodeModel
        fields = ['zip_code']

###################################################

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']