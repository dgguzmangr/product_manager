from django.db import models

class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=False, null=False)
    percentage = models.DecimalField('Long', max_digits=3, decimal_places=2, blank=False, null=False)
    status = models.BooleanField('Status', default=False, blank=False, null=False)

    class Meta:
        app_label = 'authApp'