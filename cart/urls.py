from django.urls import path
# Import views from current directory
from . import views

urlpatterns = [
    # Empty path indicates it is root URL
    # Render index view from views.py, name it "home"
    path('', views.view_cart, name="view_cart"),
    path('add<item_id>/', views.add_to_cart, name="add_to_cart"),
]
