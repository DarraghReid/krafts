from django.shortcuts import render


def view_cart(request):
    """ Render shopping cart page """

    return render(request, 'cart/cart.html')
