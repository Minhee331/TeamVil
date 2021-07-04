from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('team_detail/<int:project_id>', views.team_detail, name = "team_detail"),
    path('team_search/', views.team_search, name = "team_search"),
    path('team_search_back/', views.team_search_back, name = "team_search_back"),
    path('team_detail_back/<int:project_id>', views.team_detail_back, name = "team_detail_back"),
]