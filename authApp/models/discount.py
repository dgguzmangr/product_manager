from django.db import models

class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    date = date = models.DateField('Date', auto_now_add=True, blank=False, null=False)
    amount = models.DecimalField('Long', max_digits=3, decimal_places=2, blank=False, null=False)
    status = models.BooleanField('Status', default=False, blank=False, null=False)

    class Meta:
        app_label = 'authApp'