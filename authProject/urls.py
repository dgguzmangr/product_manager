"""
URL configuration for authProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for Product Manager",
        contact=openapi.Contact(email="dgguzmangr@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # product urls
    path('show-products/', appView.show_products),
    path('create-product/', appView.create_product),
    path('update-product/<int:pk>/', appView.update_product),
    path('delete-product/<int:pk>/', appView.delete_product),
    path('show-product-prices/<int:pk>/', appView.show_product_prices),
    path('show-product-footprint/<int:pk>/', appView.show_product_footprint),
    path('show-product-discounts/<int:pk>/', appView.show_product_discounts),
    path('show-product-taxes/<int:pk>/', appView.show_product_taxes),

    # footprint urls
    path('show-footprints/', appView.show_footprints),
    path('create-footprint/', appView.create_footprint),
    path('update-footprint/<int:pk>/', appView.update_footprint),
    path('delete-footprint/<int:pk>/', appView.delete_footprint),

    # price urls
    path('show-prices/', appView.show_prices),
    path('create-price/', appView.create_price),
    path('update-price/<int:pk>/', appView.update_price),
    path('delete-price/<int:pk>/', appView.delete_price),

    # Discount urls
    path('show-discounts/', appView.show_discounts),
    path('create-discount/', appView.create_discount),
    path('update-discount/<int:pk>/', appView.update_discount),
    path('delete-discount/<int:pk>/', appView.delete_discount),

    # Tax urls
    path('show-taxes/', appView.show_taxes),
    path('create-tax/', appView.create_tax),
    path('update-tax/<int:pk>/', appView.update_tax),
    path('delete-tax/<int:pk>/', appView.delete_tax),

    # Business Model url
    path('field-structure-view/', businessModelView.field_structure_view),

    # token
    path('generate_token/', views.obtain_auth_token),

    #login
    path('login/', appView.login),
]

# http://localhost:8000/swagger/