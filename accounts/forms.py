from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    
    First_Name = forms.CharField(max_length=15, required=True)
    Last_Name = forms.CharField(max_length=10, required=True)
    Mail = forms.EmailField(required=True)
    
    
    username = forms.CharField(max_length=150, required=True, help_text="Required. 150 characters or fewer.")

    class Meta:
        model = User
        fields = ("username", "First_Name", "Last_Name", "Mail", "password1", "password2")


class Login_Form(AuthenticationForm):
    pass 

