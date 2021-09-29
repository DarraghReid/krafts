from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """
        Setup method called whenever instance of class is created
        """

        # Assign request as attribute of class to access Stripe requests
        self.request = request

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
        print(intent)
        # Take event sent from Stripe, return 'received' http response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        # Take event sent from Stripe, return 'received' http response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
