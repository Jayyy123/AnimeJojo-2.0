from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name = "loginPage"),
    path('logout/', views.logoutPage, name = "logout"),
    path('signup/', views.signupPage, name='signupPage'),
    path('test/', views.test, name='test'),
    path('profile/', views.profile, name='profile'),
    path('profileupdate/<str:pk>/', views.profileUpdate, name='profileUpdate'),
    path('profiledelete/<str:pk/', views.profileDelete, name='profiledelete'),
]