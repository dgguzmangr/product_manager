from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) # comentar par deshabilitar seguridad
from rest_framework.authtoken import views
from authApp.views import appView
from authApp.views import businessModelView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import TokenAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Product Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # product urls
    path('show-products/', appView.show_products, name='List all created products'),
    path('create-product/', appView.create_product, name='Create a new product'),
    path('update-product/<int:pk>/', appView.update_product, name='Update a selected product'),
    path('partial-update-product/<int:pk>/', appView.partial_update_product, name='Update a selected attribute for a product'),
    path('delete-product/<int:pk>/', appView.delete_product, name='Delete a selected product'),
    path('show-product-prices/<int:pk>/', appView.show_product_prices, name='List all prices by products'),
    path('show-product-footprint/<int:pk>/', appView.show_product_footprint, name='List all footprints by products'),
    path('show-product-discounts/<int:pk>/', appView.show_product_discounts, name='List all discounts by products'),
    path('show-product-taxes/<int:pk>/', appView.show_product_taxes, name='List all taxes by products'),
    path('product-detail/<int:pk>/', appView.product_detail, name='Show product detalis'),

    # footprint urls
    path('show-footprints/', appView.show_footprints, name='List all created footprints'),
    path('create-footprint/', appView.create_footprint, name='Create a new footprint'),
    path('update-footprint/<int:pk>/', appView.update_footprint, name='Update a selected footprint'),
    path('partial-update-footprint/<int:pk>/', appView.partial_update_footprint, name='Update a selected attribute for a footprint'),
    path('delete-footprint/<int:pk>/', appView.delete_footprint, name='Delete a selected footprint'),

    # price urls
    path('show-prices/', appView.show_prices, name='List all created prices'),
    path('create-price/', appView.create_price, name='Create a new price'),
    path('update-price/<int:pk>/', appView.update_price, name='Update a selected price'),
    path('partial-update-price/<int:pk>/', appView.partial_update_price, name='Update a selected attribute for a price'),
    path('delete-price/<int:pk>/', appView.delete_price, name='Delete a selected price'),

    # Discount urls
    path('show-discounts/', appView.show_discounts, name='List all created discounts'),
    path('create-discount/', appView.create_discount, name='Create a new discount'),
    path('update-discount/<int:pk>/', appView.update_discount, name='Update a selected discount'),
    path('partial-update-discount/<int:pk>/', appView.partial_update_discount, name='Update a selected attribute for a discount'),
    path('delete-discount/<int:pk>/', appView.delete_discount, name='Delete a selected discount'),

    # Tax urls
    path('show-taxes/', appView.show_taxes, name='List all created taxes'),
    path('create-tax/', appView.create_tax, name='Create a new tax'),
    path('update-tax/<int:pk>/', appView.update_tax, name='Update a selected tax'),
    path('partial-update-tax/<int:pk>/', appView.partial_update_tax, name='Update a selected attribute for an tax'),
    path('delete-tax/<int:pk>/', appView.delete_tax, name='Delete a selected tax'),

    # Business Model url
    path('products-manager-field-structure/', businessModelView.products_field_structure_view, name='Generate a json structure for all models'),

    # token
    path('generate_token/', views.obtain_auth_token, ),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/admin/
# http://localhost:8000/swagger/
# http://localhost:8000/redoc/