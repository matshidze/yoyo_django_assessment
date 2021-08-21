from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('weather', views.WeatherView)

urlpatterns = [
    path('', include(router.urls)),
]
