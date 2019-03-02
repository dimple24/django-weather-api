from django.urls import include, path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.home),
    path('fetchData', views.weather_data, name='post_list'),
    path('weatherdata/startDate=<startDate>&endDate=<endDate>&metricType=<metricType>&location=<location>', views.WeatherDataDetail.as_view(), name='year')
]