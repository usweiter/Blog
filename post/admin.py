from django.contrib import admin
from .models import ModelPost

@admin.register(ModelPost)
class AdminPost(admin.ModelAdmin):
    pass
