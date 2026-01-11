from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm,login_form



# Create your views here.
def signup_view(request):
    
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("homepage")
    else:
        form=SignUpForm()
    
    return render(request,'accounts/signup.html',{"form":form})

def if_call_accounts(request):
    return redirect('signup')

def Home_view(request):
    return render(request,'accounts/homepage.html')

def login_view(request):
    if request.method == 'POST':
        form = login_form(request, data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = login_form()

    return render(request, 'accounts/login.html', {'form': form})





