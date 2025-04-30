from django.urls import path
from .views import products, products_detail

urlpatterns = [
    path('products/', products, name='products'), 
    path('products/<int:product_id>/', products_detail, name='products_detail')
]
