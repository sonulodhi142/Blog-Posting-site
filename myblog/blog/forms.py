from django import forms
from .models import blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['name', 'text', 'photo']

class userForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')

