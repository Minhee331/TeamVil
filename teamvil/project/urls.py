from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('team_detail/', views.team_detail, name = "team_detail"),
    path('team_search/', views.team_search, name = "team_search"),
    path('team_search_back/', views.team_search_back, name = "team_search_back"),
]