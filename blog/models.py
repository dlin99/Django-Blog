from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

from markdown_deux import markdown
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(date_posted__lte=timezone.now())


    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    read_time = models.IntegerField(default=0, null=True, blank=True) #models.TimeField(null=True, blank=True)

    # postobjects = PostObjects()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    @property
    def short_description(self):
        return truncatechars(self.content, 250)
