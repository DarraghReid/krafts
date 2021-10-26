from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Set app default_auto_field & name
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
