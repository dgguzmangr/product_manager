from django.db import models
from djmoney.models.fields import MoneyField

class Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    amount = MoneyField('Amount', max_digits=10, decimal_places=2, default_currency='USD', blank=False, null=False)
    date = models.DateField('Date', auto_now_add=True, blank=False, null=False)
    status = models.BooleanField('Status', default=False, blank=False, null=False)

    class Meta:
        app_label = 'authApp'
