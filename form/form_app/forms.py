from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')