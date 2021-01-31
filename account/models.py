from django.db import models
from django.contrib.auth.models import User

class ModelProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile')

    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile/photos/avatar/%Y/%m/%d/',
        default='profile/photos/default/profile_photo_default.jpg')
    background = models.ImageField(upload_to='profile/photos/background/%Y/%m/%d/',
        default='profile/photos/default/profile_photo_default.jpg')
    description = models.CharField(max_length=150, blank=True)
    about = models.CharField(max_length=150, blank=True)
