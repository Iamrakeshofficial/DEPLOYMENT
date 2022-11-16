from django.apps import AppConfig


class BloggingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Blogging'

    def ready(self):
        import Blogging.signals
