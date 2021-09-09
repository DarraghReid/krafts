from django.shortcuts import render
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
