from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Set app default_auto_field & name
    Override ready() method
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # Override ready() method
    def ready(self):
        # import signals module
        import checkout.signals
