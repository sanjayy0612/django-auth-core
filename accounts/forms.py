from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):

    #Name
    First_Name=forms.CharField( max_length=15, required=True)
    Last_Name=forms.CharField(, max_length=10, required=True)

    #Gmail
    Mail=forms.forms.EmailField(, required=True)

    

    class meta():
        model=User
        fields=("First_Name","Last_Name","Mail")


