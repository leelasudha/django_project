from django.urls import path
from . import views

urlpatterns = [path("", views.index),path("add_products", views.add_products), 
path("show_products", views.show_products)]
