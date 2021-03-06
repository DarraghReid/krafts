from django.urls import path
# Import views from current directory
from . import views
from .webhooks import webhook

urlpatterns = [
    # Render checkout view from views.py, name it "checkout"
    path('', views.checkout, name="checkout"),
    path(
        'checkout_success/<order_number>',
        views.checkout_success, name="checkout_success"),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name="webhook"),
]
