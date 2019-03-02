from django.db import models

# Create your models here.
class WeatherData(models.Model):
    # id = models.IntegerField(primary_key=True, default=0)
    rainfall = models.FloatField(default=0.0)
    max_temp = models.FloatField(default=0.0)
    min_temp = models.FloatField(default=0.0)
    month = models.IntegerField(default=0)
    year = models.IntegerField()
    location= models.CharField(default="",max_length=10)
    
    class Meta:
        verbose_name_plural = "weatherData"