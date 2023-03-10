from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('my_account/', views.my_account, name="my_account"),
    # path('delete/<int:pk', DeleteView.as_view(), name="delete-user")

]