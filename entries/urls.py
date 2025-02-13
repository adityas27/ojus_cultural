from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('sports/', views.sport_events, name="all_sports"),
    path('cultural/', views.cultural_events, name="all_cultural"),
    path('cultural/<str:events>/', views.cultural_events_details, name="cultural_details"),
    path('sports/<str:sport>/', views.sport_events_details, name="sports_details"),
    path('register/', views.register, name="register"),
]