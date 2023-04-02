from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import  messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.app.forms import UserRegisterForm, UserLoginForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, 'Account created successfully')
        return valid

    def form_invalid(self, form):
        messages.error(self.request, 'Error creating account')
        return super().form_invalid(form)



class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

