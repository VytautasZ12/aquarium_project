from django.apps import AppConfig


class AquariumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aquarium'

    def ready(self):
        from .signals import create_profile, save_profile
