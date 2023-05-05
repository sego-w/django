from django.apps import AppConfig


class WhaaatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin