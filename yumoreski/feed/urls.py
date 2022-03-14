from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('add', views.add, name='add')
]
