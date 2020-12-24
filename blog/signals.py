from django.db.models.signals import pre_save
from .models import Post
from .utils import get_read_time



def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)
