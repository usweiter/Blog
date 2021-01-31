from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class ModelPost(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'), ('test', 'Test'))
    title = models.CharField(max_length=250, blank=True)
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    img = models.ImageField(blank=True, upload_to='post/%Y/%m/%d/')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        default=STATUS_CHOICES[1][0],
        choices=STATUS_CHOICES,
        blank=True)
    tags = TaggableManager(blank=True, help_text=False)

    def get_absolute_url(self):
        return reverse('post:post', args=[self.id])

    class Meta:
        ordering = ("-published", )

    def __str__(self):
        return self.text

    objects = models.Manager()
    issued = PublishedManager()
