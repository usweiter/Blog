from django.contrib import admin
from .models import ModelProfile

@admin.register(ModelProfile)
class AdminProfile(admin.ModelAdmin):
    pass
    