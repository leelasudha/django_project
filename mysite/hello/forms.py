from django import forms
from hello.models import *
class ProductsForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ["product_id","product_code","product_name","description"]