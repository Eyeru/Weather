from django.shortcuts import render, get_object_or_404
from .models import Weather
import requests
from .forms import AreaForm


def index(request):
    api_key = 'YOUR TOKEN'
    form = AreaForm() 
    if request.method == 'POST':
           form = AreaForm(request.POST) 
           if form.is_valid(): 
               form.save()

    location = Weather.objects.all()
    weather_info = []
    for l in location:
        area_weather = requests.get(api_key.format(l)).json() 

        weather = {
            'location' : l,
            'temperature' : area_weather['main']['temp'],
            'description' : area_weather['weather'][0]['description'],
        }
        weather_info.append(weather) 
    context = {'weather_info' : weather_info, 'form' : form}

    return render(request, 'index.html', context)
