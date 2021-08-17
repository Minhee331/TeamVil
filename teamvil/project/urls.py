from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('team_detail/<int:project_id>', views.team_detail, name = "team_detail"),
    path('team_search/', views.team_search, name = "team_search"),
    path('team_search_back/', views.team_search_back, name = "team_search_back"),
    path('team_search_back_cloud/', views.team_search_back_cloud, name = "team_search_back_cloud"),
    path('team_detail_back/<int:project_id>', views.team_detail_back, name = "team_detail_back"),
    path('team_new_back_S/', views.team_new_back_S, name="team_new_back_S"),
    path('team_new_back_S_if/', views.team_new_back_S, name="team_new_back_S"),
    path('team_new_back_C/', views.team_new_back_C, name="team_new_back_C"),
    path('team_new_back_P/', views.team_new_back_P, name="team_new_back_P"),
    path('upload_project_file/<int:project_id>', views.upload_project_file, name = 'upload_project_file'),
    path('team_create_back_S/', views.team_create_back_S, name="team_create_back_S"),
    path('team_create_back_C/', views.team_create_back_C, name="team_create_back_C"),
    path('team_create_back_P/', views.team_create_back_P, name="team_create_back_P"),
    path('searchTeam/', views.searchTeam, name="searchTeam"),
    path('filterTeam/', views.filterTeam, name="filterTeam"),
    path('popularTeam/', views.popularTeam, name="popularTeam"),
    path('latestTeam/', views.latestTeam, name="latestTeam"),
    path('like/',views.like, name="like"),
    path('likecancel/',views.likecancel, name = "likecancel"),
    path('scrap/', views.scrap, name="scrap"),
    path('scrapcancels/',views.scrapcancel, name="scrapcancel"),
    path('team_application/',views.team_application, name = "team_application"),
    path('team_review/<int:project_id>', views.team_review, name = "team_review"),
    path('team_review_form/', views.team_review_form, name="team_review_form"),
    path('team_apply_form_back/<int:project_id>',views.question_form, name="question_form"),
    path('team_apply/<int:project_id>', views.team_apply, name="team_apply"),
    path('team_apply_modify_back/<int:project_id>', views.team_apply_modify, name="team_apply_modify"), 
    # path('team_answer_form_back_sunneng/<int:question_id>',views.answer_form, name="answer_form"),
    path('classify_A/', views.classify_A, name="classify_A"),
    path('classify_S/', views.classify_S, name="classify_S"),
    path('classify_C/', views.classify_C, name="classify_C"),
    path('classify_P/', views.classify_P, name="classify_P"), 

    # kay
    path('team_new/', views.team_new, name = "team_new"),
    path('team_form/', views.team_form, name = "team_form"),
]