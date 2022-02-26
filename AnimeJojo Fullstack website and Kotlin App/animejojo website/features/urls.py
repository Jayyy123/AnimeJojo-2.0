from django.urls import path
from . import views

urlpatterns = [
    path('', views.features, name = "features"),
    path('wallpapers/', views.wallpapers, name = "wallpapers"),
    path('animequiz/', views.animeQuiz, name = "animequiz"),
    path('random/', views.randomAnime, name = "random"),
    path('characterize/', views.characterize, name = "characterize"),
]