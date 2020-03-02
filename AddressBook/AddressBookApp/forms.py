from __future__ import unicode_literals

from django.db import models
from django import forms
from AddressBookApp.models import AddressBookApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class AddressBookForm(ModelForm):
    class Meta:
        model= AddressBookApplication
        fields=['first_name' ,'last_name' ,'phone_number','email_address','zip_code','city','state','notes']
        
class UpdateAddressBookForm(ModelForm):
    class Meta:
        model = AddressBookApplication
        fields = ['first_name' ,'last_name','phone_number','zip_code','city','state','notes']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=250, help_text='Required. Inform a valid email address.') 
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'first_name', 'last_name', 'email')

