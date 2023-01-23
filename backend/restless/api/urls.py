from django.urls import path
from . import views

urlpatterns = [
    path('quotes/',views.api_home, name='test')
]