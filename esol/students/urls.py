from django.urls import path
from . import views
from .views import Learners


urlpatterns = [
    path('learners/', views.Learners, name='learners-page'),
]
