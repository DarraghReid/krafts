from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """ Show all products, along with sorting options and search queries """

    # Get all products from the db
    products = Product.objects.all()

    # Context dictionary is passed into product.html for use
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Show individual product details """

    # Get product from db using the product's id
    product = get_object_or_404(Product, pk=product_id)

    # Context dictionary is passed into product_detail.html for use
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
