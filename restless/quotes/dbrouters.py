from .models import *


class MyDBRouter(object):
    def db_for_read(self, model, **hints):
        if model == Author or model == Quotes:
            return 'quotes'
        return None

    def db_for_write(self, model, **hints):
        if model == Author or model == Quotes:
            return 'quotes'
        return None
