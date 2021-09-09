from django.urls import path
# Import views from current directory
from . import views

# Include these urls in project level urls.py

urlpatterns = [
    # Render all_products view
    path('', views.all_products, name="products"),
]
