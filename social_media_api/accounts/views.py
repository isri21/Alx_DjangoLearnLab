from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from accounts.serializers import UserCreationSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate, get_user_model
from .functions import get_token
from rest_framework import status
from .models import User
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import generics
from accounts.models import User as CustomUser

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
@permission_classes([permissions.IsAuthenticated])	
def profile(request):
	try:
		user = request.user
		profile = UserProfileSerializer(user)
		
		return Response(profile.data, status=status.HTTP_200_OK)
	except Exception:
		return Response({"error": "An Error Occured"}, status=status.HTTP_400_BAD_REQUEST)
	

class Follow(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		follow = CustomUser.objects.get(id=kwargs.get("user_id"))
		user = request.user
		user.following.add(follow)
		follow.followers.add(user)

		return Response({"status": f"You have followed {follow}"}, status=status.HTTP_200_OK)

class UnFollow(generics.GenericAPIView):
	permission_classes = [permissions.IsAuthenticated]
	def post(self, request, *args, **kwargs):
		unfollow = CustomUser.objects.get(id=kwargs.get("user_id"))
		user = request.user
		user.following.remove(unfollow)
		unfollow.followers.remove(user)

		return Response({"status": f"You have followed {unfollow}"}, status=status.HTTP_200_OK)
	
	


			