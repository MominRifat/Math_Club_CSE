from django.urls import path
from . import views

urlpatterns = [
    path('active/', views.active_team, name='active_team'),
    path('former/', views.former_presidents, name='former_presidents'),
]
