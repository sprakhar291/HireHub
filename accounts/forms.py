from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email', 'user_type', 'password1', 'password2')
