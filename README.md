# django-weather-api

Installation steps:
1. Go to the mysite folder where requirements.txt is located and run command pip install requirements.txt
2. I have used mysql database, please change connections according to your DB and its client
3. Inside virtual environment of django, make migrations using command <python manage.py makemigrations> and then for migrating run 
    <python manage.py migrate>
    This will create Table schema according to the models in the database mentioned in settings file.
4. Run the server using command <python manage.py runserver> and hit url in browser http://localhost:8000/ 
5. Click on link FetchData inserts the data in table schema
        For first time you need to fetch data and save it inside DB and only after that above API will fetches data from that DB
  
6. GET URL: http://localhost:8000/weatherdata/startDate=<startDate>&endDate=<endDate>&metricType=<metricType>&location=<location>
    where <startDate>, <endDate> format = "yyyy-mm"
           <metricType> = "Rainfall", "Tmax", "Tmin"
           <location> = "UK", "England", "Scotland", "Wales"
               
    Eg: http://127.0.0.1:8000/weatherdata/startDate=2015-01&endDate=2017-12&metricType=Rainfall&location=UK
    
          
