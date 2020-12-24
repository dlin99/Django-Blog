from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    # overwrite the method for signals
    def ready(self):
    	import blog.signals
