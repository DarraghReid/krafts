from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import Order, OrderForm
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .models import OrderLineItem
from cart.contexts import cart_contents
import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ Add meta data key to payment intent that confirmCardPayment
    doesn't support. Sent from stripe_elements.js """
    try:
        # Split client secret to get payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Set up Stripe with secret key to modify payment intent
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modify PI: pass in pid, specify data to be modified
        stripe.PaymentIntent.modify(pid, metadata={
            # Json dump of cart
            'cart': json.dumps(request.session.get('cart', {})),
            # User's save info preference
            'save_info': request.POST.get('save_info'),
            # User submitting form
            'username': request.user,
        })
        return HttpResponse(status=200)
    # In case of error
    except Exception as e:
        # Add error message
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        # Display error content & bad request status
        return HttpResponse(content=e, status=400)


def checkout(request):
    # Get public and secret keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # If the request is POST
    if request.method == 'POST':
        # Get cart from session
        cart = request.session.get('cart', {})

        # Insert form data in form_data dictionary
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Create instance of form using form_data dictionary above
        order_form = OrderForm(form_data)

        # If the form is valid
        if order_form.is_valid():
            # Save the order, preventing multiple save events
            order = order_form.save(commit=False)
            # Split client secret to get payment intent id
            pid = request.POST.get('client_secret').split('_secret')[0]
            # Set order's stripe_pid to pid
            order.stripe_pid = pid
            # Set order's orignal_cart to json string version of cart
            order.original_cart = json.dumps(cart)
            # Save order
            order.save()

            # For each item in the cart
            for item_id, item_data in cart.items():
                try:
                    # Find the product in the db
                    product = Product.objects.get(id=item_id)
                    # Create order line item using product information
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    # Save order_line_item
                    order_line_item.save()

                # If no product is found
                except Product.DoesNotExist:
                    # Display error message
                    messages.error(request, (
                        "One of the products in your cart wasn't \
                        found in our database. "
                        "Please call us for assistance!")
                    )

                    # Delete the order
                    order.delete()

                    # Return user to cart
                    return redirect(reverse('view_cart'))

            # Save user's preference to save their info to session
            request.session['save_info'] = 'save-info' in request.POST

            # Redirect user to checkout_success page
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))

        # If the form is invalid
        else:
            # Inform user of error
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    # If the request is GET
    else:
        # Get cart from session
        cart = request.session.get('cart', {})
        # If cart is empty
        if not cart:
            # Use error message to inform user the cart is empty
            messages.error(
                request, "There's nothing in your cart at the moment")
            # Bring user back to products page
            return redirect(reverse('products'))

        # Access cart_contents' contexts dictionary from cart's context.py
        current_cart = cart_contents(request)
        # Save grand_total's key from dictionary to total variable
        total = current_cart['grand_total']
        # Convert total to integer for Stripe
        stripe_total = round(total * 100)
        # Set secret key on Stripe
        stripe.api_key = stripe_secret_key
        # Create payment intent
        intent = stripe.PaymentIntent.create(
            # Set the amount to stripe_total above
            amount=stripe_total,
            # Set the currency to value of STRIPE_CURRENCY in settings
            currency=settings.STRIPE_CURRENCY
        )

        # If the user is authenticated
        if request.user.is_authenticated:
            try:
                # Get their profile
                profile = UserProfile.objects.get(user=request.user)
                # Create instance of order form pre filled with user's info
                order_form = OrderForm(initial={
                    # Name and email retrieved from user account
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    # Other data retrieved from default profile info
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            # If user can't be found
            except UserProfile.DoesNotExist:
                # Create empty instance of order form
                order_form = OrderForm()
        # If user is not authenticated
        else:
            # Create empty instance of order form
            order_form = OrderForm()

    # If stripe_public_key has not been set
    if not stripe_public_key:
        # Prompt for public key to be set
        messages.warning(
            request, 'Stripe public key is missing.\
                Did you forget to set it in your environment?')

    # Create template for checkout form
    template = 'checkout/checkout.html'

    # Pass order form into context
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Render the template with order form
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    # Get user's preference whether to save their info from session
    save_info = request.session.get('save_info')

    # Get order using order number to send to template
    order = get_object_or_404(Order, order_number=order_number)

    # If the user is authenticated, profile created along w/ account
    if request.user.is_authenticated:
        # Get user's profile
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        # Save order
        order.save()

        # Save the user's info:
        # If save info box was checked, keys match user profile model
        if save_info:
            # Compile user's profile data from order
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }

            # Create instance of user profile form w/ profile data
            # to update profile
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            # Save form if valid
            if user_profile_form.is_valid():
                user_profile_form.save()

    # Inform user that the order has been processed successfully,
    # provide them with their order number and a confrimation email
    # has been sent
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Delete redundant cart from the session
    if 'cart' in request.session:
        del request.session['cart']

    # Set template to return user to
    template = 'checkout/checkout_success.html'

    # Insert order into context
    context = {
        'order': order,
    }

    # Render template with context passed in
    return render(request, template, context)
