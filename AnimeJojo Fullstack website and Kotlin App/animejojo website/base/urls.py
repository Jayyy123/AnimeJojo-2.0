from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home1"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('allanime/', views.allAnime, name='allanime'),
    path('slideshow/', views.slideshow, name='slideshow')
]