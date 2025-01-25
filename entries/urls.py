from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.events_all, name="all_events"),
    path('<str:sport>/', views.event_details, name="event_details"),
    path('register/', views.register, name="register"),

]