from django.shortcuts import render
from .models import WeatherData
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherDataSerializer
import datetime
import requests

class WeatherDataDetail(APIView):
    def get(self, request, startDate, endDate, metricType, location):
        
        start = startDate.split("-")
        end = endDate.split("-")

        weatherList = WeatherData.objects.filter(
            year__gt=start[0], year__lt=end[0], month__gt=start[1], month__lt=end[1], location = location
        )
        serializer = WeatherDataSerializer(weatherList, many=True)
        return Response(serializer.data)

def home(request):
    return render(request, "app/index.html")

def weather_data(request):
    url = "https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{metric}-{location}.json"
    for loc in ["UK", "England", "Scotland", "Wales"]:
        for met in ["Rainfall", "Tmax", "Tmin"]:
            r = requests.get(url.format(metric=met, location=loc)).json()
            for t in range(len(r)):
                print("--------------------------------")
                print(t, r[t]["value"], r[t]["year"], r[t]["month"])
                print("--------------------------------")
                try:
                    obj = WeatherData.objects.get(
                        location=loc, year=r[t]["year"], month=r[t]["month"]
                    )
                    if met == "Tmax":
                        obj.max_temp = r[t]["value"]
                        print("Max temp value: ", obj.max_temp)
                    elif met == "Tmin":
                        obj.min_temp = r[t]["value"]
                        print("Min temp value: ", obj.min_temp)

                    obj.save()
                except WeatherData.DoesNotExist:
                    print("Not Found")
                    WeatherData(
                        location=loc,
                        Rainfall=r[t]["value"],
                        year=r[t]["year"],
                        month=r[t]["month"],
                    ).save()

                    print("Rainfall value: ", WeatherData.Rainfall)

    return render(request, "app/index.html")

