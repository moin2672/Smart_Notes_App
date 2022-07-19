from django.urls import path
from django.views import View

from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
]