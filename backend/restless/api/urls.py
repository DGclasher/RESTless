from .views import *
from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('fetch/quote/',QuotesListView.as_view(), name='fetch-quotes'),
    path('fetch/author/all/', AuthorListView.as_view(), name="fetch-author-all"),
    path('fetch/author/', views.api_author, name="fetch-author-all"),
    path('create/quote/', QuotesCreateView.as_view(), name="create-quote"),
    path('create/author/', AuthorCreateView.as_view(), name="create-author"),
    path('update/author/<int:pk>', AuthorUpdateView.as_view(), name="update-author"),
    path('delete/author/<int:pk>', AuthorDeleteView.as_view(), name="delete-author"),
    path('delete/quote/<int:pk>', QuotesDeleteView.as_view(), name="delete-quote")

]