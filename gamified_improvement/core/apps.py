from django.apps import AppConfig


# core/apps.py
class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        import core.models  # This ensures signals are registered

