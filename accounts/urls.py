# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path("home/",views.Home_view,name="homepage"),
    path("",views.if_call_accounts,name='accounts'),
    path("login/",views.login_view,name="login"),
    path('logout/', views.logout_view, name='logout'),

]