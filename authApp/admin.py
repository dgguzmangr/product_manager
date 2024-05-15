from django.contrib import admin

from .models.product import Product
from .models.footprint import Footprint
from .models.price import Price
from .models.discount import Discount

admin.site.register(Product)
admin.site.register(Footprint)
admin.site.register(Price)
admin.site.register(Discount)
# Register your models here.
