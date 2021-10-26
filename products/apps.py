from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Set app default_auto_field & name
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
