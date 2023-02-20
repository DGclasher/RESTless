from django.contrib.auth.models import User, Group, Permission
from rest_framework.authtoken.models import Token


class MyDBRouter(object):
    def db_for_read(self, model, **hints):
        if model == User or model == Group or model == Permission or model==Token:
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        if model == User or model == Group or model == Permission or model==Token:
            return 'users'
        return None
