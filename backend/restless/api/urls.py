from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

urlpatterns = [
    path('fetch/quote/',QuotesListView.as_view(), name='fetch-quotes'),
    path('fetch/author/all/', AuthorListView.as_view(), name="fetch-author-all"),
    path('fetch/author/', views.api_author, name="fetch-author-all"),
    path('create/quote/', views.api_quote_post, name="create-quote"),
    path('create/author/', AuthorCreateView.as_view(), name="create-author"),
    # path('update/quote/<int:pk>', AuthorUpdateView.as_view(), name="update-quote"),
    path('update/author/<int:pk>', AuthorUpdateView.as_view(), name="update-author"),
    path('delete/author/<int:pk>', AuthorDeleteView.as_view(), name="delete-author")

]