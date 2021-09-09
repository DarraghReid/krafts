from django.urls import path
# Import views from current directory
from . import views

urlpatterns = [
    # Empty path indicates it is root URL
    # Render index view from views.py, name it "home"
    path('', views.index, name="home"),
]
