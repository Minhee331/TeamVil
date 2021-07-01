from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('member_search_back/', views.member_search_back, name = "member_search_back"),
]