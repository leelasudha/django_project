from django.contrib import admin
from .models import employee
# Register your models here.

admin.site.register(employee)


#serialise class:- it convert your model(employee) to JSON data
