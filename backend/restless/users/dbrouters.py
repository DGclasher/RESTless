from django.contrib.auth.models import User


class MyDBRouter(object):
    def db_for_read(self, model, **hints):
        if model == User:
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        if model == User:
            return 'users'
        return None
