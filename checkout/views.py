from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get cart from session
    cart = request.session.get('cart', {})
    # If cart is empty
    if not cart:
        # Use error message to inform user the cart is empty
        messages.error(request, "There's nothing in your cart at the moment")
        # Bring user back to products page
        return redirect(reverse('products'))

    # Create instance of order form
    order_form = OrderForm()
    # Create template for checkout form
    template = 'checkout/checkout.html'
    # Pass order form into context
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdE8kIG08sq5PbneZfPMis2xT3h1YVUG3QACZEo6QLVpSCMIVMFnE3LbKUcMTPyYu6Cg4SBLSDvIcCuG8ZYaTar00RvOr9djV',
        'client_secret': 'test client secret'
    }

    # Render the template with order form
    return render(request, template, context)