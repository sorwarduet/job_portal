from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


# Create your views here.
from .form import AccountRegisterForm
from .models import Account

class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = Account
    success_url = '/'
    success_message = "Your user account has been created"
    
