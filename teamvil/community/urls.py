from typing import Pattern
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('community_list/', views.community, name="community_list"),
    path('community_detail/<int:community_id>', views.community_detail, name="community_detail"),
    path('commnunity_new/', views.community_new, name="community_new")
]