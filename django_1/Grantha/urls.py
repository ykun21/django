from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Grantha-home"),
    path('about', views.about, name="Grantha-about"),
    path('browse', views.browse, name="Grantha-browse")
]
