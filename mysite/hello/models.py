from django.db import models

# Create your models here.
class Products(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_code = models.CharField(max_length = 256)
	product_name = models.CharField(max_length=256)
	description = models.CharField(max_length=256)
	
