from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterFrom
    success_message = "Your profile has been created successfully"