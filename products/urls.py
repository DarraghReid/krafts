from django.urls import path
# Import views from current directory
from . import views

# Include these urls in project level urls.py

urlpatterns = [
    # Render all_products view
    path('', views.all_products, name="products"),
    # Product id should be integer to avoid confusion with add/ url
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    # path('<int:product_id>/<int:reply_comment>', views.reply_comment, name="reply_comment"),
    path('add/', views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name="edit_product"),
    path('delete/<int:product_id>/', views.delete_product, name="delete_product"),
    path('remove/<int:comment_id>/', views.delete_comment, name="delete_comment"),
]
