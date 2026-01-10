from django.contrib.forms import UserCreationForm
from django import forms
from django.contrib.auth.Models import User


class SignUpForm(UserCreationForm):

    #Name
    First_Name=forms.CharField(, max_length=15, required=True)
    Last_Name=forms.forms.CharField(, max_length=10, required=True)

    #Gmail
    Mail=forms.forms.EmailField(, required=True)

    #password

    Password=forms.forms.CharField(, max_length=20, required=True)

    class meta():
        model=User
        fields=("First_Name","Last_Name","Mail","Password")


