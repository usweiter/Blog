from django.db import models
from post.models import ModelPost
from django.contrib.auth.models import User

class ModelComment(models.Model):
	post = models.ForeignKey(ModelPost, on_delete=models.CASCADE, related_name="comments")
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
	text = models.CharField(max_length=250)

	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return f'Author of comment: {self.author}.'