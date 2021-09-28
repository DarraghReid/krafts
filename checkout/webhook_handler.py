from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # Setup method called whenever instance of class is created
    def __init__(self, request):
        # Assign request as attribute of class to access Stripe requests
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)