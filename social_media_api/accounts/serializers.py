from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class UserCreationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True)
	class Meta:
		model = get_user_model()
		fields = ["username", "email", "password", "password2"]

	def validate(self, data):
		if data["password"] != data["password2"]:
			raise serializers.ValidationError("Passwords do not match!!!")
		return data
	
	def create(self, validated_data):
		validated_data.pop("password2")
		user = get_user_model().objects.create_user(**validated_data)
		user.save()
		Token.objects.create(user=user)
		return user
	
	def update(self, instance, validated_data):
		validated_data.pop("password2")
		for field, value in validated_data.items():
			setattr(instance, field, value)
		instance.save()
		return instance
	
class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
	followers = serializers.StringRelatedField(many=True)
	following = serializers.StringRelatedField(many=True) 
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name", "followers", "following"]