from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):

    #Name
    First_Name=forms.CharField( max_length=15, required=True)
    Last_Name=forms.CharField( max_length=10, required=True)

    #Gmail
    Mail=forms.EmailField(required=True)

    

    class Meta():
        model=User
        fields=("First_Name","First_Name","Last_Name","Mail")


class Login_Form(AuthenticationForm):
    pass 

