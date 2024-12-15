from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .permissions import IsOwner
from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get_permissions(self):
		if self.action in ["update", "partial_update", "destroy"]:
			return [IsOwner]
		if self.action == "create":
			return [permissions.IsAuthenticated]
		return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])	
def feed(request):
	following = request.user.following.all()
	posts = Post.objects.filter(author__in=following)
	serialized = PostSerializer(posts, many=True)
	return Response(serialized.data, status=status.HTTP_200_OK)



