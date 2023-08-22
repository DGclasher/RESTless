from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from rest_framework.authtoken.models import Token
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    form_class = LoginForm

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterFrom
    success_url = reverse_lazy('login')
    success_message = "Profile created successfully"

class DeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete_user_confirm.html'
    success_message = "Profile deleted successfully"
    success_url = reverse_lazy('home')

    def delete(self, *args, **kwargs):
        pass


@login_required
def my_account(request):
    token = Token.objects.get(user=request.user)
    print(token)
    return render(request, "frontend/my_account.html", {
        "token" : token
    })
