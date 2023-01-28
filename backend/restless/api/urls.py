from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

urlpatterns = [
    path('quotes/',views.api_quotes, name='quotes'),
    path('author/', views.api_author, name="author")
]