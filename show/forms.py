from django import forms
from .models import *
from django.contrib.auth.models import User


class Imageform(forms.ModelForm):

    class Meta:
        model=Product
        fields=['name','desc','category','img','amount']

class UserSignupform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model=StoreUser
        fields=['username','roles']  

class UserSigninform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=StoreUser
        fields=['username',]  

class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','desc']

class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone','concern']