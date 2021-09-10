from django.contrib import admin

from .models import Product
from .models import Category


# ModelAdmin is built in
class ProductAdmin(admin.ModelAdmin):
    # list_display tuple tells admin which fields to display in admin
    list_display = (
        'pk',
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
