from django.shortcuts import render

from products.models import Product

# Create your views here.

def products(request):
    product = Product.objects.all()
    return render(request=request, template_name='products/products.html', context={'products': product})    

def products_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    return render(request=request, template_name='products/product_detail.html', context={'product' : product})
    