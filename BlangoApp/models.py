from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Custom manager to handle published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISH)

class Post(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'df', 'draft'
        PUBLISH = 'pb', 'published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField(max_length=1000)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager()  # Default manager instance
    published = PublishedManager()  # Custom manager instance
    
    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]
    
    def __str__(self):
        return self.title
