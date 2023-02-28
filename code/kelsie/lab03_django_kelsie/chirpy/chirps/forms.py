from django import forms

class ChirpForm(forms.form):
    text = forms.CharField(label="Chirp", max_length=128)
    