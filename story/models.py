from django.db import models
from django.contrib.auth.models import User

class ModelStory(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='stories')
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='stories/%Y/%m/%d/')
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)