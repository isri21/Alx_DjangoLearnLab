from rest_framework import serializers
from accounts.models import User
class UserCreationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ["username", "email", "password", "password2"]

	def validate(self, data):
		if data["password"] != data["password2"]:
			raise serializers.ValidationError("Passwords do not match!!!")
		return data
	
	def create(self, validated_data):
		validated_data.pop("password2")
		user = User.objects.create_user(**validated_data)
		user.save()
		return user
	
	def update(self, instance, validated_data):
		validated_data.pop("password2")
		for field, value in validated_data.items():
			setattr(instance, field, value)
		instance.save()
		return instance
	
class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=100)
	password = serializers.CharField(max_length=100)

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name"]