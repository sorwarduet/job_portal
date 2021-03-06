from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
from .form import AccountRegisterForm
from .models import Account

class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/user-register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = "Your user account has been created"

    def form_valid(self, form):
        user=form.save(commit=False)
        user_type =form.cleaned_data['user_types']

        if user_type == 'is_employee':
            user.is_employee = True
        elif user_type == 'is_employer':
            user.is_employer = True
        
        user.save()

        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
   pass
    

class UserView(TemplateView):
    template_name = 'users/user-register.html'