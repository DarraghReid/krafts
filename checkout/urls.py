from django.urls import path
# Import views from current directory
from . import views

urlpatterns = [
    # Render checkout view from views.py, name it "checkout"
    path('', views.checkout, name="checkout"),
]
