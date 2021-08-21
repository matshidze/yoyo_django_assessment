from rest_framework import serializers
from .models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Mate:
        model = Weather
        fields = ('maximum', 'minimum', 'average', 'mediam')
