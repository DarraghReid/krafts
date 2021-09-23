# For Django to send signals after model instance is saved/deleted
from django.db.models.signals import post_save, post_delete
# To recieve signals
from django.dispatch import receiver
# OrderLineItem listening for signals
from .models import OrderLineItem


# Execute function when post_save signal is sent
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    # Access order line item related to, call update_total on it
    instance.order.update_total()


# Execute function when post_delete signal is sent
@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    # Access order line item related to, call update_total on it
    instance.order.update_total()
