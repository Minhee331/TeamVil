from typing import Pattern
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('community_list_back/', views.community_list_back, name="community_list_back"),
    path('community_detail_back/<int:community_id>', views.community_detail_back, name="community_detail_back"),
    path('community_new_back/', views.community_new_back, name="community_new_back"),
    path('community_new/', views.community_new, name="community_new"),
    path('community_detail_content/<int:community_id>', views.community_detail_content, name = "community_detail_content"),
    path('comment/', views.comment, name="comment"),
    path('reply/', views.reply, name="reply"),
    path('register_info/', views.register_info, name="register_info"),
    path('info/', views.info, name="info"),
    path('info_detail/<int:info_id>', views.info_detail, name="info_detail"),



    # kay
    path('community/', views.community, name="community"),
]