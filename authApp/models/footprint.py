from django.db import models
from .product import Product

class Footprint(models.Model):
    UNITS = [
        ('Gramo', 'Gramo'),
        ('Kilogramo', 'Kilogramo'),
        ('Tonelada', 'Tonelada'),
        ('Mililitro', 'Mililitro'),
        ('Litro', 'Litro'),
        ('Metro cúbico', 'Metro cúbico'),
        ('Metro', 'Metro'),
        ('Centímetro', 'Centímetro'),
        ('Metro cuadrado', 'Metro cuadrado'),
        ('Palet', 'Palet'),
        ('Caja', 'Caja'),
        ('Paquete', 'Paquete'),
        ('Botella', 'Botella'),
        ('Barril', 'Barril'),
        ('Contenedor', 'Contenedor'),
    ]

    footprint_id = models.AutoField(primary_key=True)
    measurement_unit = models.CharField('Measurement unit', max_length=70, choices=UNITS, blank=False, null=False)
    long = models.DecimalField('Long', max_digits=10, decimal_places=3, blank=False, null=False)
    high = models.DecimalField('High', max_digits=10, decimal_places=3, blank=False, null=False)
    width = models.DecimalField('Width', max_digits=10, decimal_places=3, blank=False, null=False)
    weight = models.DecimalField('Weight', max_digits=10, decimal_places=3, blank=False, null=False)
    volume = models.DecimalField('Volume', max_digits=10, decimal_places=3, blank=True, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='footprint')

    def save(self, *args, **kwargs):
        self.volume = self.long * self.high * self.width
        super(Footprint, self).save(*args, **kwargs)

    class Meta:
        app_label = 'authApp'
