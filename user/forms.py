from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import UserProfile
from django.forms import  TextInput, EmailInput, FileInput, Select


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label= 'Username:')
    first_name = forms.CharField(max_length=100, help_text='First Name', label= 'First Name:')
    last_name  = forms.CharField(max_length=100, help_text='Last Name', label= 'Last Name:')
    email = forms.EmailField(max_length=200, label='Email:')
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
          user.save()
        return user



class UserUpdateForm(UserChangeForm):
  class Meta:
    model = User
    fields = ('username','first_name', 'last_name', 'email')
    widgets = {
      'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
      'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
      'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}),
      'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Email Adress'}),
    }



STATE = [
  ('Abia', 'Abia'),
  ('Edo', 'Edo'),
  ('Imo', 'Imo'),
  ('Lagos', 'Lagos'),
  ('Oyo', 'Oyo'),
  ('ondo', 'Ondo'),
  ('Rivers', 'Rivers')
]

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    fields = ('phone', 'address', 'city','state', 'country', 'image')
    widgets ={
      'first_name': TextInput(attrs={'class':'input', 'placeholder':'First Name'}),
      'last_name': TextInput(attrs={'class':'input', 'placeholder':'Last Name'}),
      'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone'}),
      'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
      'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
      'state': Select(attrs={'class': 'input', 'placeholder': 'State'}, choices=STATE),
      'country': TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
      'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
    }
    
    
