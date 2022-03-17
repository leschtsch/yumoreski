from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register', views.CreateUser.as_view(), name='register'),
    path('login', include('django.contrib.auth.urls'), name='login')
]
