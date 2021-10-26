from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Add/edit line items in admin from inside Order model
    """
    # Access OrderLineItem (see inlines var in OrderAdmin below)
    model = OrderLineItem
    # lineitem_total not to be edited
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for orders
    """
    # Access OrderLineItem from OrderAdmin interface in Admin
    inlines = (OrderLineItemAdminInline,)

    # Fields caculated by model method, read only so they cannot be edited
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid',)

    # Specify order of fields in admin interface
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
              'stripe_pid',)

    # Fields displayed in admin
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # Fields order by date from newest to oldest
    ordering = ('-date',)


# Register Order, OrderAdmin models (OrderLineItem through OrderAdmin)
admin.site.register(Order, OrderAdmin)
