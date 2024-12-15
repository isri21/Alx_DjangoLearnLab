from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


user = get_user_model()
# Create your models here.
class Notification(models.Model):
	recepient = models.ForeignKey(user, on_delete=models.CASCADE, related_name="notified")
	actor = models.ForeignKey(user, on_delete=models.CASCADE, related_name="notify")
	verb = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	target = GenericForeignKey("content_type", "object_id")

	def __str__(self):
		return f"Notification for {self.recipient.username}"