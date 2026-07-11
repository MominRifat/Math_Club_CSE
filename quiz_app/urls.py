from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz'), 
    path('take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
    path('leaderboard/', views.leaderboard_home, name='leaderboard_home'),
    path('leaderboard/<int:quiz_id>/', views.quiz_leaderboard, name='quiz_leaderboard'),
]