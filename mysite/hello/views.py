from django.shortcuts import render,redirect
from django.http import HttpResponse
from hello.forms import ProductsForm
from hello.models import Products

# Create your views here.
def index(request):
	return HttpResponse("Hello world!")
def add_products(request):
	if request.method == "POST":
		form = ProductsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/show_products')
	form = ProductsForm()
	return 	render(request, 'add_products.html', {'form' : form})
def show_products(request):
	products = Products.objects.all()
	return render(request, 'show_products.html',{'products': products})