from django.urls import path
from . import views
from .views import teacherInfo, teacherProfile, Home, about


urlpatterns = [
    path ('', views.Home, name='home-page'),
    path ('accounts/profile/', views.Home, name='home-page'),
    path ('about/', views.about, name='about-page'),
    path ('teacher/', views.teacherInfo, name='teachers-page')
    ]
