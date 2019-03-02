from rest_framework import serializers
from . import models
from .models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData 
        fields = ("id", "rainfall", "max_temp", "min_temp", "month", "year","location",)
        
