
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls'), name='frontend'),
    path('users/', include("users.urls"), name='users'),
    path('api/', include('api.urls'), name='api'),
    path('quotes/', include('quotes.urls'), name='quotes')
]

urlpatterns += staticfiles_urlpatterns()
