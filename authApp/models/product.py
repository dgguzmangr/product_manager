from django.db import models
from .footprint import Footprint
from .price import Price
from .discount import Discount
import uuid

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    sku = models.CharField('SKU', max_length=100, blank=True, null=False)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    short_description = models.CharField('Short description', max_length=30, blank=False, null=False)
    long_description = models.CharField('Long description', max_length=100, blank=False, null=False)
    footprint = models.OneToOneField(Footprint, on_delete=models.CASCADE, related_name='product')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='product')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, related_name='product')

    class Meta:
        app_label = 'authApp'

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_unique_sku()
        super().save(*args, **kwargs)

    def generate_unique_sku(self):
        return str(uuid.uuid4()).replace('-', '')[:10]
