from django.apps import AppConfig


class WeedSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weed_site'

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'
