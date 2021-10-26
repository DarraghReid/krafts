from django.apps import AppConfig


class ContactConfig(AppConfig):
    """
    Set app default_auto_field & name
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
