from django.urls import path
from . import views
from .views import scedule


urlpatterns = [
    path('scedule/', views.scedule, name='classes-scedule')
]
