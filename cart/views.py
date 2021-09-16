from django.shortcuts import render, redirect


def view_cart(request):
    """ Render shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add an item to cart """

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
    # Otherwise, add item along with quantity from form
    else:
        cart[item_id] = quantity

    # Put cart variable into session
    request.session['cart'] = cart

    print(request.session['cart'])

    # Redirect user back to redirect_url
    return redirect(redirect_url)
