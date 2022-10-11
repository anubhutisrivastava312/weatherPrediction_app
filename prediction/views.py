
from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def home(request):
    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' +city+ '&units=metric&appid=e3c9fd165eb1503cba9fd27ade36dddf').read()
        list_of_data=json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        return render(request,'prediction/html/home.html',data)
        
    
    
    return render(request,'prediction/html/home.html')