from django.urls import path
from . import views
from .views import lession_c



urlpatterns = [
    path('lessions/', views.lession_c, name="lessions-page"),
    path('lessions/groups', views.lession_group, name="groups-page")
]
