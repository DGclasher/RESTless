from rest_framework import generics
from .models import *
from .serializers import *

class QuotesDetailAPIView(generics.RetrieveAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuoteSerializer

class QuotesCreateAPIView(generics.CreateAPIView):
    querset = Quotes.objects.all()
    serializer_class = QuotePostSerializer

class AuthorDetailsView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer