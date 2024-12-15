from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="posts")
	title = models.CharField(max_length=150)
	content = models.TextField(max_length=500)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.title
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
	author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="comments_author")
	content = models.TextField(max_length=500)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	def __str__(self):
		return self.content[:20]