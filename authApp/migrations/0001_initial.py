# Generated by Django 4.1.13 on 2024-05-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(blank=True, max_length=100, verbose_name='SKU')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('short_description', models.CharField(max_length=30, verbose_name='Short description')),
                ('long_description', models.CharField(max_length=100, verbose_name='Long description')),
            ],
        ),
    ]
