from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'frontend/home.html')
