from django.db.models.signals import pre_save
from .models import Post
from .utils import get_read_time
from django.utils.text import slugify



def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):

	if not instance.slug:
		instance.slug = create_slug(instance)


	if instance:
		html_string = instance.get_markdown()
		read_time_var = get_read_time(html_string)
		instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)
