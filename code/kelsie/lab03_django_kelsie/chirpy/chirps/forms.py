from django import forms
from .models import ImgModel

class ChirpForm(forms.ModelForm):
    caption = forms.CharField(max_length=128)
    my_image = forms.ImageField()

    class Meta:
        model = ImgModel
        fields = ["caption", "my_image"]