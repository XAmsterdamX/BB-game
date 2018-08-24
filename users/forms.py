# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'organization')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'organization')


class InstructorRequestForm(forms.Form):
        your_first_name = forms.CharField(label='First name', max_length=100)
        your_surname = forms.CharField(label='Surname', max_length=100)
        your_organization = forms.CharField(label='Organization', max_length=100, required=False)
        your_username = forms.CharField(label='Username', max_length=100)
        your_email = forms.EmailField(label='Email', max_length=200)

