from django.contrib import admin

from .models.product import Product
from .models.footprint import Footprint
from .models.price import Price

admin.site.register(Product)
admin.site.register(Footprint)
admin.site.register(Price)
# Register your models here.
