from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get_permissions(self):
		if self.action in ["update", "partial_update", "destroy"]:
			return [IsOwner]
		if self.action == "create":
			return [IsAuthenticated]
		return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
