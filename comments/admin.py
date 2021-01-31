from django.contrib import admin
from .models import ModelComment

@admin.register(ModelComment)
class AdminComment(admin.ModelAdmin):
	pass