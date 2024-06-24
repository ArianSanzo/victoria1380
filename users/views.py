from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return self.request.POST.get('next', reverse_lazy('products:list'))

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('products:list')