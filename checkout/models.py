import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product


# Each order will be created according to this model, as input by user
class Order(models.Model):
    # Order number automatically generated, should not be edited
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    # Use CountryField imported above
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    # auto_now_add automatically sets order date and time w/ every new order
    date = models.DateTimeField(auto_now_add=True)
    # Three fields calculated using model method when order is saved
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    # Original cart that created order to allow duplicate orders to be added
    original_cart = models.TextField(null=False, blank=False, default='')
    # Unique cart payment id to allow duplicate orders to be added
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID (imported above)
        """
        # Generate random 32 character string
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added, called each time
        line item added to order
        """
        # Get sum of order's lineitem_total fields
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # If the order_total lower than FREE_DELIVERY_THRESHOLD
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            # Delivery cost - add STANDARD_DELIVERY_PERCENTAGE to order_total
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        # Otherwise, there is no delivery cost
        else:
            self.delivery_cost = 0
        # Grand total is order_total plus delivery_cost (if any)
        self.grand_total = self.order_total + self.delivery_cost
        # Save order
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the default save method to set order number
        if it hasn't been set already.
        """
        # If order being saved doesn't have order number
        if not self.order_number:
            # Generate order number
            self.order_number = self._generate_order_number()
        # Save order
        super().save(*args, **kwargs)

    # String method takes in Order model, returns order number
    def __str__(self):
        return self.order_number


# OrderLineItem created for each cart item, then attached to/updates Order
class OrderLineItem(models.Model):
    # Line item's order. related_name allows access to line items from Order
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    # Line item's product, quantity, total cost
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    # Automatically calculated when line item is saved, should not be edited
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        # lineitem_total is product price times quantity
        self.lineitem_total = self.product.price * self.quantity
        # Save
        super().save(*args, **kwargs)

    # String method returns line item product's sku and order number
    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
