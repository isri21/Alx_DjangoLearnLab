from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="posts")
	title = models.CharField(max_length=150)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	
class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")
	author = models.ForeignKey(user, on_delete=models.CASCADE, related_name="comments_author")
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.content[:20]
	

class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
	user = models.ForeignKey(user, on_delete=models.CASCADE, related_name="liked_post")

	def __str__(self):
		return f"{self.post.title} | {self.user.username}"
