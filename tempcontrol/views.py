from django.shortcuts import render
from tempcontrol import sensor
from tempcontrol import untappd


def home(request):
	return render(request, 'tempcontrol/home.html')


def get_temperature(request):
	return render(request, 'tempcontrol/get_temperature.html', {
	    'temp': sensor.retrieve_temp(),
	})


def get_beer_style(request):
	return


def run_autocomplete(request):
	input_name = request.GET['q']

	return render(request, 'tempcontrol/beer_suggestions.html', {
	    'matched': untappd.search_beer(input_name),
	})
