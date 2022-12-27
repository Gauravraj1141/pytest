from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User_Blog


# user register


class User_register_form(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label="Password (Re-enter)")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}), label="Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        labels = {"email": "Email"}
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }


# User login form

class User_login_form(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))


# create a user blog for write his own blog so we give here model form
class User_blog_form(forms.ModelForm):

    class Meta:
        model = User_Blog
        fields = ['Title', 'Desc', ]

        widgets = {
            'Title': forms.TextInput(attrs={"class": "form-control"}),
            'Desc': forms.Textarea(attrs={"class": "form-control"}),
        }
