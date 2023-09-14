from django.contrib import admin
from django.urls import path, include
from weather_app import views

app_name = 'weather_app'

urlpatterns = [
    path('', views.index, name="index"),
]
