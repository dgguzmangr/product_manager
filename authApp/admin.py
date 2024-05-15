from django.contrib import admin
from .models.product import Product
from .models.footprint import Footprint

admin.site.register(Product)
admin.site.register(Footprint)
# Register your models here.
