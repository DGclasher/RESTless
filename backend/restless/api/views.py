from django.shortcuts import render
from django.http import JsonResponse
from quotes.models import *
import json

def api_home(request, *args, **kwargs):
    quote=Quotes.objects.all().order_by("?").first()
    data={}
    data['quote'] = quote.quote
    data['author'] = quote.author

    return JsonResponse(data)
