from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.


def all_products(request):
    """ Show all products, along with sorting options and search queries """

    # Get all products from the db
    products = Product.objects.all()

    # Initialise as None to prevent errors
    query = None

    # Check if request is GET
    if request.GET:
        # Check if 'q' is in the request
        # ('q' name of text input of search bar)
        if 'q' in request.GET:
            # Assign value of 'q' to query
            query = request.GET['q']
            # If query is blank and returns no results
            if not query:
                # Attach error message to request
                messages.error(
                    request, "You didn't enter any search criteria!")
                # redirect to product url
                return redirect(reverse('products'))
            # If query not blank, contruct name/description queries using Q obj
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # Use queries to filter products in the database
            products = products.filter(queries)

    # Context dictionary is passed into product.html for use
    context = {
        'products': products,
        'search_term': query,
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
