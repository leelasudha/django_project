from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight,Passenger
# Create your views here.
def index(request):
	#return HttpResponse("Flights")
	context = { "flights" : Flight.objects.all()}
	return render(request, 'flights/index.html', context)
def flight(request, flight_id):
	try:
		flight = Flight.objects.get(pk=flight_id)
		print(flight.id)
		print(Passenger.objects.exclude(flights=flight).all())
	except Flight.DoesNotExist:
		raise Http404("Flight Does not exist")
	context = {"flight": flight, "passenger": flight.passengers.all(), "non_passengers": Passenger.objects.exclude(flights=flight.id).all()}
	return render(request, "flights/flight.html", context)
def book(request, flight_id):
	try:
		passenger_id = int(request.POST['passenger'])
		passenger = Passenger.objects.get(pk= passenger_id)
		flight = Flight.objects.get(pk=flight_id)
	except KeyError:
		return render(request, "flights/error.html", {'message': "No selection"})
	except Flight.DoesNotExist:
		return render(request, "flights/error.html", {'message': "No Flight"})
	except Passenger.DoesNotExist:
		return render(request, "flights/error.html", {'message': "No Passengers"})
	passenger.flights.add(flight)
	return HttpResponseRedirect(reverse('flight', args = (flight_id,)))
