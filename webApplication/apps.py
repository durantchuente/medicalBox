from django.apps import AppConfig


class WebapplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webApplication'
    
    def ready(self):
        import webApplication.signals