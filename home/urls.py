from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('home', views.home),
    path('authorized', views.authorized),
]