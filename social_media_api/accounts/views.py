from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import UserCreationSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate, get_user_model
from .functions import get_token
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(["POST"])
def register(request):
	serialized = UserCreationSerializer(data=request.data)
	if serialized.is_valid(raise_exception=True):
		serialized.save()
		user = User.objects.get(username=serialized.validated_data["username"])
		token = Token.objects.get(user=user)
		return Response({"token": token.key})

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
	try:
		user = request.user
		profile = UserProfileSerializer(user)
		
		return Response(profile.data, status=status.HTTP_200_OK)
	except Exception:
		return Response({"error": "An Error Occured"}, status=status.HTTP_400_BAD_REQUEST)
	
@api_view(["POST"])
@permission_classes([IsAuthenticated])	
def follow(request, user_id):
	if request.method == "POST":
		follow = get_user_model().objects.get(id=user_id)
		user = request.user
		user.following.add(follow)
		follow.followers.add(user)

		return Response({"status": f"You have followed {follow}"}, status=status.HTTP_200_OK)
	

@api_view(["POST"])
@permission_classes([IsAuthenticated])	
def unfollow(request, user_id):
	if request.method == "POST":
		unfollow = get_user_model().objects.get(id=user_id)
		user = request.user
		user.following.remove(unfollow)
		unfollow.followers.remove(user)

		return Response({"status": f"You have unfollowed {unfollow}"}, status=status.HTTP_200_OK)
	


			