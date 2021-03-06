from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
# Django checks if user logged in before executing view
# If not, user is redirected to login page
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm


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
    """ Show individual products / render comments form """

    # Get user for initial data
    user = request.user

    # Get product from db using the product's id
    product = get_object_or_404(Product, pk=product_id)

    # Set initial data to prefill form
    initial_data = {
        'product': product,
        'name': user,
    }

    # Create instance of product form, insert initial data
    form = CommentForm(initial=initial_data)

    # Create instance of Product Form for rating
    product_form = ProductForm(instance=product)

    # Context dictionary is passed into product_detail.html for use
    context = {
        'product': product,
        'form': form,
        'product_form': product_form,
    }

    return render(request, 'products/product_detail.html', context)


def add_comment(request, product_id):
    """ Add comments to individual products """

    # Get product from db using the product's id
    product = get_object_or_404(Product, pk=product_id)

    # Get the contents of form
    form = CommentForm(request.POST)

    # If form is valid
    if form.is_valid():
        # Save it
        form.save()

        # Display success message to user
        messages.success(request, 'Comment successfully posted!')

    # If form is not valid
    else:
        # Display error message to the user
        messages.error(
            request,
            'Failed to add comment. Please ensure the form is valid.')

    # Redirect to new product's detail page using product's id
    return redirect(reverse('product_detail', args=[product.id]))


def reply_comment(request, product_id, comment_id):
    """ Allow admin to reply
        to product comments """

    # Get product from db using the product's id
    product = get_object_or_404(Product, pk=product_id)

    # Get parent comment from db using the comment's id
    comment = get_object_or_404(Comment, pk=comment_id)

    # Get the contents of form
    form = CommentForm(request.POST)

    # If form is valid
    if form.is_valid():
        # Save it
        new_comment = form.save(commit=False)
        new_comment.name = request.user
        new_comment.product = product
        new_comment.parent = comment
        new_comment.save()

        # Display success message to user
        messages.success(request, 'Reply successfully posted!')

        # Redirect to new product's detail page using product's id
        return redirect(reverse('product_detail', args=[product.id]))

    # If form is not valid
    else:
        # Display error message to the user
        messages.error(
            request,
            'Failed to add reply. Please ensure the form is valid.')

    return render(request, 'products/product_detail.html')


@login_required
def edit_comment(request, comment_id, product_id):
    """ Edit a comment in the store """

    # Get product
    product = get_object_or_404(Product, pk=product_id)

    # Get comment
    comment = get_object_or_404(Comment, pk=comment_id)

    # Instantiate, pre-fill form, specifying comment to be edited
    form = CommentForm(request.POST, instance=comment)

    # If the form is valid
    if form.is_valid():
        # Save it
        form.save()

        # Display success message to user
        messages.success(request, 'Successfully edited comment!')

        # Redirect user to the inividual comment's details page
        return redirect(reverse('product_detail', args=[product.id]))

    # If the form is not valid
    else:
        # Display error message to user
        messages.error(
            request,
            'Failed to update comment. Please ensure the form is valid.')


@login_required
def add_product(request):
    """ Add a product to the store """

    # If user is not a superuser
    if not request.user.is_superuser:
        # Inform user they are not authorised to add a product
        messages.error(request, 'Sorry, only store owners can do that.')
        # Redirect user back to home page
        return redirect(reverse('home'))

    # If request method is POST
    if request.method == 'POST':
        # Get form, capture image file
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
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')

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


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    # If user is not a superuser
    if not request.user.is_superuser:
        # Inform user they are not authorised to edit a product
        messages.error(request, 'Sorry, only store owners can do that.')
        # Redirect user back to home page
        return redirect(reverse('home'))

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
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
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


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    # If user is not a superuser
    if not request.user.is_superuser:
        # Inform user they are not authorised to delete a product
        messages.error(request, 'Sorry, only store owners can do that.')
        # Redirect user back to home page
        return redirect(reverse('home'))

    # Get product to be deleted
    product = get_object_or_404(Product, pk=product_id)

    # Remove product from db
    product.delete()

    # Inform user product has been deleted
    messages.success(request, 'Product deleted!')

    # Return user to Products page
    return redirect(reverse('products'))


@login_required
def delete_comment(request, comment_id):
    """ Delete a comment from the store """

    # Get comment to be deleted
    comment = get_object_or_404(Comment, pk=comment_id)

    # Get comment's related product (to redirect to its detail page)
    product = comment.product

    # Remove comment from db
    comment.delete()

    # Inform user comment has been deleted
    messages.success(request, 'Comment deleted!')

    # Redirect to new product's detail page using product's id
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def rate_product(request, product_id):
    """ Add rating to product """

    # Get product
    product = get_object_or_404(Product, pk=product_id)

    # Get user
    user = request.user

    # Add user to rates list
    product.rates.add(user)

    # Get the contents of form
    form = ProductForm(request.POST, instance=product)

    # Get product's current rating
    current_rating = product.rating

    # If the form is valid
    if form.is_valid():
        # Get user's rating
        user_rating = form.cleaned_data['rating']

        # Get number of users who have rated product
        user_count = product.rates.count()

        # Calculate sum total of user ratings
        total_rating = user_rating + current_rating

        # Check if product has any rates to prevent division error
        if user_count > 0:
            # Average rating is total_rating divided by user_count
            average_rating = total_rating / user_count
        else:
            average_rating = 0

        # Save form to variable (difficulty accessing product.rating)
        new_rating = form.save(commit=False)

        # Update product's rating
        new_rating.rating = user_rating + current_rating

        # Update product's average rating
        new_rating.rating_average = average_rating

        # Save the form
        new_rating.save()

        # Display success message to user
        messages.success(request, 'You rated this product!')

        # Redirect user to the inividual product's details page
        return redirect(reverse('product_detail', args=[product.id]))

    # If the form is not valid
    else:
        # Display error message to user
        messages.error(
            request,
            'Failed to update product. Please ensure the form is valid.')

    # Redirect to new product's detail page using product's id
    return redirect(reverse('product_detail', args=[product.id]))
