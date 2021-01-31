from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class ModelImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    created = models.DateField(auto_now_add=True, db_index=True)
    url = models.URLField()
    users_like = models.ManyToManyField(User, related_name='images_like', blank=True)