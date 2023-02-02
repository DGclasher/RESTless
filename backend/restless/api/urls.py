from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

urlpatterns = [
    path('fetch/quotes/quote/',views.api_quotes, name='quotes'),
    path('fetch/quotes/author/', views.api_author, name="author"),
    path('quotes/post/', views.api_quote_post, name="quote_post"),
    path('quotes/post/author/', views.api_post_author, name="author_post"),

]