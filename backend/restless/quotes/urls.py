from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('details/quote/<int:pk>/' , QuotesDetailAPIView.as_view(), name='detail-view' ),
    path('create/' , QuotesCreateAPIView.as_view(), name='create-view' ),
    path('details/author/<int:pk>',AuthorDetailsView.as_view(), name="all-authors")
]