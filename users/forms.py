from django import forms

from .validators import rule_email
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.forms import TextInput, EmailInput, FileInput, Select


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           validators=[MinLengthValidator(2)])
    email = forms.EmailField(validators=[rule_email])
    message = forms.CharField(widget=forms.Textarea)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': TextInput({'class': 'textinput form-control',
                                          'placeholder': 'username'}),
                   'email': EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }


from .models import Account
class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phone', 'address','vk','instagram','telegram', 'account_image']
        widgets = {'phone': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'phone number'}),
                   'address': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'address'}),
                   'vk': TextInput({'class': 'textinput form-control',
                                      'placeholder': 'vk'}),
                   'instagram': TextInput({'class': 'textinput form-control',
                                         'placeholder': 'instagram'}),
                   'telegram': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'telegram'}),
                   'account_image': FileInput({'class': 'form-control',
                                       'placeholder': 'image'})
                   }
