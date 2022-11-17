from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))



class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "שם משתמש",
                "class": "form-control"
            }
        ))
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "מספר טלפון",
                "class": "form-control"
            }
        ))
    office = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "משרד",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'office')
