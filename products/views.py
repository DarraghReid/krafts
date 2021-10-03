from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ Show all products, along with sorting options and search queries """

    # Get all products from the db
    products = Product.objects.all()

    # Initialise variables as None to prevent errors
    query = None
    categories = None
    sort = None
    direction = None

    # Check if request is GET
    if request.GET:
        # If 'sort' is in the request
        if 'sort' in request.GET:
            # Assign 'sort' to sortkey
            sortkey = request.GET['sort']
            # Assign value of sortkey to sort variable to preserve "name" field
            sort = sortkey

            # Using annotation, create a temporary field (lower_name) to
            # sort on (instead of "name") for case-insensitive sorting

            # If the value of sortkey is "name"
            if sortkey == "name":
                # Reassign it to lower_name
                sortkey = "lower_name"
                # Create temp field of all products in lower case to sort on
                products = products.annotate(lower_name=Lower('name'))
            # If the value of sortkey is "category"
            if sortkey == "category":
                # Specify that it is sorted by category name
                sortkey == "category__name"

            # If 'direction' is also in the request
            if 'direction' in request.GET:
                # Assign its value to direction variable
                direction = request.GET['direction']
                # If direction's value is descending
                if direction == 'desc':
                    # Reverse the order of sortkey
                    sortkey = f'-{sortkey}'
            # Sort products using order_by model method
            products = products.order_by(sortkey)

        # If 'category' is in the request
        # ('catergory' name of url parameter in dropdown nav-links)
        if 'category' in request.GET:
            # Split it into list
            categories = request.GET['category'].split(",")
            # Use list to filter all products in the db with those categories
            products = products.filter(category__name__in=categories)
            # Get selected categories' objects for user confirmation
            categories = Category.objects.filter(name__in=categories)

        # If 'q' is in the request
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
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            # Use queries to filter products in the database
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    # Context dictionary is passed into product.html for use
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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

def add_product(request):
    """ Add a product to the store """

    # If request method is POST
    if request.method == 'POST':
        # Create instance of product form, capture image file
        form = ProductForm(request.POST, request.FILES)

        # If form is valid
        if form.is_valid():
            # Save it, store product in product variable
            product = form.save()

            # Display success message to user
            messages.success(request, 'Successfully added product!')

            # Redirect to new product's detail page using product's id
            return redirect(reverse('product_detail', args=[product.id]))

        # If form is not valid
        else:
            # Display error message to the user
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    # Otherwise
    else:
        # Create instance of product form
        form = ProductForm()

    # Get template to render
    template = 'products/add_product.html'

    # Create context to pass into form
    context = {
        'form': form,
    }

    # Render form along with context
    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    # Get product
    product = get_object_or_404(Product, pk=product_id)

    # If the request is POST
    if request.method == 'POST':
        # Instantiate, pre-fill form, specifying product to be edited
        form = ProductForm(request.POST, request.FILES, instance=product)

        # If the form is valid
        if form.is_valid():
            # Save it
            form.save()

            # Display success message to user
            messages.success(request, 'Successfully updated product!')

            # Redirect user to the inividual product's details page
            return redirect(reverse('product_detail', args=[product.id]))

        # If the form is not valid
        else:
            # Display error message to user
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    # If the request is not POST
    else:
        # Populate the form with product information
        form = ProductForm(instance=product)

        # Inform user that they are editing the product
        messages.info(request, f'You are editing {product.name}')

    # Get template to render form
    template = 'products/edit_product.html'

    # Create context to be passed to template
    context = {
        'form': form,
        'product': product,
    }

    # Render template along with context
    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    # Get product to be deleted
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from db
    product.delete()

    # Inform user product has been deleted
    messages.success(request, 'Product deleted!')

    # Return user to Products page
    return redirect(reverse('products'))
