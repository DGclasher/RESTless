import random
from quotes.models import *
from quotes.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import authentication_classes, permission_classes

class StandardResultSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50

def pick_random_object():
    return random.randrange(1, Quotes.objects.all().count()+1)


class QuotesListView(generics.ListAPIView):
    serializer_class = QuotesSerializer
    authentication_classes = []
    permission_classes = []
    def get_queryset(self):
        return Quotes.objects.all().filter(id=pick_random_object())


class QuotesCreateView(generics.CreateAPIView):
    serializer_class = QuotesCUDSerializer
    queryset = Quotes.objects.all()

class QuotesDeleteView(generics.DestroyAPIView):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.high_auth_quote:
            return Response({"message" : "Not allowed on that quote"})
        self.perform_destroy(instance)
        return Response({"message" : "Quote deleted successfully"})

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultSetPagination
    authentication_classes = []
    permission_classes = []


class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if (instance.high_auth):
            return Response({'message': 'Not allowed on that author'})
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        result = {
            "message": "success",
            "details": serializer.data,
            "status": 200
        }
        return Response(result)


class AuthorDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if (instance.high_auth):
            return Response({'message': 'Not allowed on that author'})
        self.perform_destroy(instance)
        return Response({"message": "Author deleted successfully"})


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def api_author(request, *args, **kwargs):
    obj = request.GET
    data = {}
    if (obj.get('name') and obj.get('id')):
        return Response({'message': 'Only allowed to send name or id, not both'})
    try:
        if (obj.get('name')):
            ath = Author.objects.get(name=obj.get('name'))
        elif (obj.get('id')):
            ath = Author.objects.get(id=obj.get('id'))
        else:
            return Response({'message': 'Unknown parameter'})
        data['id'] = ath.id
        data['name'] = ath.name
        data['quotes'] = list(ath.quote_set.all().values('id', 'quote'))
        return Response(data)

    except Author.DoesNotExist:
        return Response({'message': "Author doesn't exist"})
