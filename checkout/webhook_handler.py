from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """
        Setup method called whenever instance of class is created
        """

        # Assign request as attribute of class to access Stripe requests
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        # Get user email from order
        cust_email = order.email
        # Render confirmation_emails files to strings
        subject = render_to_string(
            # File to render
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            # Context can be accessed in confirmation_emails txt files
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        # Send the email
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            # List of email addressed email to be sent to
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        # Take event sent from Stripe, return 'received' http response
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        # Get payment intent
        intent = event.data.object
        # Get payment intent id
        pid = intent.id
        # Get cart from payment intent metadata
        cart = intent.metadata.cart
        # Get user's save info preference from pi metadata
        save_info = intent.metadata.save_info
        # Get billing details from intent
        billing_details = intent.charges.data[0].billing_details
        # Get shipping details from intent
        shipping_details = intent.shipping
        # Get grand_total from intent
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Set empty strings in shipping details to None to ensure
        # compatibility with database format
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        # Initialise profile to None to allow anon checkout
        profile = None
        # Get username from payment intent metadata
        username = intent.metadata.username
        # If user is not anonymous / is authenticated
        if username != 'AnonymousUser':
            # Get their profile
            profile = UserProfile.objects.get(user__username=username)
            # If save_info box is checked
            if save_info:
                # Set shipping details as default delivery info
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                # Save the profile
                profile.save()

        # Initialise order_exists to False
        order_exists = False
        # Counter for webhook handler attept to find order
        attempt = 1
        # Give 5 chances for order to be found
        while attempt <= 5:
            try:
                # Try to get order using payment intent info
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                # If order is found, order_exists is true
                order_exists = True
                # Break out of the loop
                break
            # If order isn't found
            except Order.DoesNotExist:
                # Increment attempt count by 1
                attempt += 1
                # Sleep for 1 second (5 seconds total to find order)
                time.sleep(1)
        # If order exists in db
        if order_exists:
            # Call _send_confirmation_email function to send email to user
            self._send_confirmation_email(order)
            # Return status 200 to Stripe, confirming order is in db
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | '
                'SUCCESS: Verified order already in database',
                status=200)
        # If order doesn't exist, create the order
        else:
            # Initialise order to None for anon users
            order = None
            # For authenticated users, try:
            try:
                # Create order using data from payment intent
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    # Set user_profile to profile variable above
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                # For each item in the json version of cart
                for item_id, item_data in json.loads(cart).items():
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
            except Exception as e:
                # In case of error
                if order:
                    # Delete order
                    order.delete()
                # Return an error 500 response to Stripe
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Call _send_confirmation_email function to send email to user
        self._send_confirmation_email(order)

        # Take event sent from Stripe, return 'received' http response
        return HttpResponse(
            content=f'Webhook received: {event["type"]} '
            '| SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Take event sent from Stripe, return 'received' http response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
