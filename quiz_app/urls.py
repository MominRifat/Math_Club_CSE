from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz'), 
    path('take/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
]