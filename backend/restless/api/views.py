from quotes.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quotes.serializers import *
from rest_framework import generics, status
import random
from django.views.decorators.csrf import csrf_exempt


def pick_random_object():
    return random.randrange(1, Quotes.objects.all().count()+1)


class QuotesListView(generics.ListAPIView):
    serializer_class = QuotesSerializer

    def get_queryset(self):
        return Quotes.objects.all().filter(id=pick_random_object())


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if(instance.high_auth):
            return Response({'message':'Not allowed on that author'})
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        result = {
            "message" : "success",
            "details" : serializer.data,
            "status" : 200
        }
        return Response(result)



class AuthorDeleteView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if(instance.high_auth):
            return Response({'message':'Not allowed on that author'})
        self.perform_destroy(instance)
        return Response({"message": "Author deleted successfully"})


@api_view(["GET"])
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
        data['name'] = ath.name
        data['quotes'] = list(ath.quote_set.all().values('id','quote'))
        return Response(data)

    except Author.DoesNotExist:
        return Response({'message': "Author doesn't exist"})


@api_view(["POST", "GET"])
def api_quote_post(request, *args, **kwargs):
    data = request.data
    print(data['author_id'])
    serializer = QuotesSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        return Response({'message': 'data created'})

    return Response({'message': "Invalid data"})
