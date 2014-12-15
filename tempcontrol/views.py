from django.shortcuts import render
from tempcontrol import sensor


def home(request):
    return render(request, 'tempcontrol/home.html')


def get_temperature(request):
    return render(request, 'tempcontrol/get_temperature.html', {
        'temp': sensor.retrieve_temp(),
    })

#def get_beer_style(request):
#	return 