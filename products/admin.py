from django.contrib import admin

from .models import Product
from .models import Category


# Register models
# ModelAdmin is built in
class ProductAdmin(admin.ModelAdmin):
    # list_display is tuple which tells admin which fields
    # to display in the admin
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'rating',
        'image',
        'image_url',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

# Register models along with their respective classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
