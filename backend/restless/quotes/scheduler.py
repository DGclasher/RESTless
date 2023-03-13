import os
import sys
import django
from decouple import config
from datetime import datetime
from django.conf import settings

user_path = config('USER_PATH')

sys.path.append(os.path.abspath("/home/" + user_path + "/backend/restless"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'restless.settings'
django.setup()
BASE_DIR = sys.path[-1]

from quotes.models import *

settings.DATABASES['quotes']['NAME'] = os.path.join(BASE_DIR, 'quotes/quotes.db')

all_quotes = Quotes.objects.all()

for quote in all_quotes:
    if quote.high_auth_quote:
        pass
    else:
        curr_month = datetime.now().month
        quote_created_month = quote.created_at.month
        if((curr_month-quote_created_month) != 0):
            quote.delete()
