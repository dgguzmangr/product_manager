# Generated by Django 4.1.13 on 2024-05-15 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_price_remove_footprint_product_id_product_footprint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Long')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='authApp.discount'),
            preserve_default=False,
        ),
    ]
