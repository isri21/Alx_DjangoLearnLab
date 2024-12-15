from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import UserCreationSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from .functions import create_token, get_token
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
@api_view(["POST"])
def register(request):
	serialized = UserCreationSerializer(data=request.data)
	if serialized.is_valid(raise_exception=True):
		serialized.save()
		token = create_token(serialized.validated_data["username"])
		return Response({"token": token})

@api_view(["POST"])	
def login(request):
	serialized = UserLoginSerializer(data=request.data)
	if serialized.is_valid(raise_exception=True):
		username = serialized.validated_data["username"]
		password = serialized.validated_data["password"]
		user = authenticate(username=username, password=password)
		if user:
			token = get_token(serialized.validated_data["username"])
			return Response(token)
		else:
			return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])	
def profile(request):
	# user = User.objects.get(request.user.username)
	# profile = UserProfileSerializer(user)
	# return Response(profile.data, status=status.HTTP_200_OK)\
	try:
		# Access the currently authenticated user
		user = request.user
		
		# If you need to serialize the user profile, ensure the correct data is passed
		# Here assuming `UserProfileSerializer` can serialize the `user` model
		profile = UserProfileSerializer(user)  # Adjust this if you need a related profile model
		
		return Response(profile.data, status=status.HTTP_200_OK)
	except Exception as e:
		# Handle any errors that might occur (e.g., user not authenticated)
		return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


			