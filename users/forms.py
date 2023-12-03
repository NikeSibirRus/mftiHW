from django import forms

from .validators import rule_email
from django.core.validators import MinLengthValidator



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators=[MinLengthValidator(2)])
    email = forms.EmailField(validators=[rule_email])
    message = forms.CharField(widget=forms.Textarea)
