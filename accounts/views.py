from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import SignUpForm,Login_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Welcome {user.username}! Account created successfully!')
            return redirect('/accounts/')  # or 'home'
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {"form": form})

def if_call_accounts(request):
    return redirect('signup')

def Home_view(request):
    return render(request,'accounts/homepage.html')

def login_view(request):
    if request.method == 'POST':
        form = Login_Form(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage') 
            messages.success(request,"Logged In ")
    else:
        form = Login_Form()

    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request,"logged Out")
    return redirect('login')
    


@login_required(login_url='login')
def Home_view(request):
    return render(request, 'accounts/homepage.html')




