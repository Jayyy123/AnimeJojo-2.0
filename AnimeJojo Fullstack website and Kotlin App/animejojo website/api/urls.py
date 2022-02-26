from django.urls import path
from . import views

urlpatterns = [
    path('', views.listLinks, name='listLinks'),
]