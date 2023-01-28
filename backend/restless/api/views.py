from quotes.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quotes.serializers import *
from rest_framework import viewsets

@api_view(["GET"])
def api_quotes(request, *args, **kwargs):
    instance=Quotes.objects.all().order_by("?").first()    
    data={}
    if instance:
        data = QuoteSerializer(instance).data
    return Response(data)

@api_view(["POST","GET"])
def api_author(request, *args, **kwargs):
    obj = request.GET
    data={}
    if(obj.get('name') and obj.get('id')):
        return Response({'detail':'Only allowed to send name or id, not both'})
    elif(obj.get('name')):
        ath = Author.objects.get(name=obj.get('name'))
    elif(obj.get('id')):
        ath = Author.objects.get(id=obj.get('id'))
    else:
        return Response({'detail':'unknown parameter'})

    data['name'] = ath.name
    data['quotes'] = list(ath.quotes_set.all().values())
    return Response(data)
   
    