from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('member_search_back/', views.member_search_back, name = "member_search_back"),
    path('member_detail_back/<int:profile_id>', views.member_detail_back, name = "member_detail_back"),
]