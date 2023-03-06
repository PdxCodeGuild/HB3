from django.forms import ModelForm
from .models import UserForm

class UserForms(ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'