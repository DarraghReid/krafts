from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ Render shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add an item to cart """

    # Get product
    product = get_object_or_404(Product, pk=item_id)

    # Get item quantity from quantity selector form input field
    quantity = int(request.POST.get('quantity'))

    # Get redirect url from hidden form input field
    redirect_url = request.POST.get('redirect_url')

    # Get or create session dictionary to store cart contents
    cart = request.session.get('cart', {})

    # Put item into cart dictionary
    # If there is a matching item already in the cart
    if item_id in list(cart.keys()):
        # Increment the item's quantity by new quantity from form
        cart[item_id] += quantity
        # Inform user item has been updated
        messages.success(
            request, f'Added { quantity } more { product.name } to your cart')
    # Otherwise, add item along with quantity from form
    else:
        cart[item_id] = quantity
        # Inform user item has been added
        messages.success(request, f'Added { product.name } to your cart!')

    # Put cart variable into session
    request.session['cart'] = cart

    # Redirect user back to redirect_url
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust item quantity """

    # Get product
    product = get_object_or_404(Product, pk=item_id)

    # Get item quantity from quantity selector form input field
    quantity = int(request.POST.get('quantity'))

    # Get or create session dictionary to store cart contents
    cart = request.session.get('cart', {})

    # Data coming from quantity selector form in cart.html
    # If there is more than one of a specific item
    if quantity > 0:
        # Set the item's quantity to that number
        cart[item_id] = quantity

        # Inform user item has been updated
        messages.success(
            request, f'Added { quantity } more { product.name } to your cart')

    # Otherwise, remove the item
    else:
        cart.pop(item_id)

        # Inform user item has been removed
        messages.success(request, f'Removed { product.name } from your cart!')

    # Put cart variable into session
    request.session['cart'] = cart

    # Redirect user back to cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove item from cart """

    try:
        # Get product
        product = get_object_or_404(Product, pk=item_id)

        # Get or create session dictionary to store cart contents
        cart = request.session.get('cart', {})

        # Remove item from cart
        cart.pop(item_id)

        # Inform user item has been removed
        messages.success(request, f'Removed { product.name } from your cart!')

        # Put cart variable into session
        request.session['cart'] = cart

        # Return http response if successfully removed
        return HttpResponse(status=200)

    except Exception as err:
        # Inform user if there has been an error removing the item
        messages.error(
            request, f'Error removing { product.name }: {err}')

        # Return any exception as 500 error
        return HttpResponse(status=500)
