from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
	actor = serializers.CharField(source="actor.username")
	class Meta:
		model = Notification
		fields = ["actor", "verb", "timestamp"]