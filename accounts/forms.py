from django import forms

# to create a form to sign up a new user and django control it
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        # from User class in django
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class UserForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput,)
    class Meta:
        # from User class in django
        model = User
        fields = ['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    # image = forms.ImageField(widget=forms.FileInput,)
    class Meta:
        # from Profile class
        model = Profile
        fields = ['image','phone_number']