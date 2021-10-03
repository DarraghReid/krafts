from django.urls import path
# Import views from current directory
from . import views

# Include these urls in project level urls.py

urlpatterns = [
    # Render all_products view
    path('', views.all_products, name="products"),
    # Product id should be integer to avoid confusion with add/ url
    path('<int:product_id>/', views.product_detail, name="product_detail"),
    path('add/', views.add_product, name="add_product"),
]
