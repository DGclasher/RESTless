from .forms import *
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.authtoken.models import Token


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    form_class = UserRegisterFrom
    success_message = "Your profile has been created successfully"


@login_required
def my_account(request):
    token = Token.objects.get(user=request.user)
    print(token)
    return render(request, "frontend/my_account.html", {
        "token" : token
    })
