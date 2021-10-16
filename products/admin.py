from django.contrib import admin

from .models import Product
from .models import Category
from .models import Comment


class ProductAdmin(admin.ModelAdmin):
    """ Tell admin which fields to display in admin """
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
    """ Tell admin which fields to display in admin """
    list_display = (
        'name',
        'friendly_name',
    )


class CommentAdmin(admin.ModelAdmin):
    """ Tell admin which fields to display in admin """
    list_display = (
        'pk',
        'name',
        'date',
        'product',
        'comment',
        'parent',
    )


# Register models along with their respective classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
