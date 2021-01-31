from django.contrib import admin
from .models import ModelStory

@admin.register(ModelStory)
class AdminStory(admin.ModelAdmin):
    pass