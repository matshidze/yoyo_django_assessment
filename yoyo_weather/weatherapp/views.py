from django.shortcuts import render
import requests
from rest_framework import viewsets
from .models import Weather
from .serialize import WeatherSerializer

# Create your views here.


class WeatherView(viewsets.ModelViewSet):

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer





