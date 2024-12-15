from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from .permissions import IsOwner
from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from rest_framework import generics
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
	following_users = request.user.following.all()
	posts = Post.objects.filter(author__in=following_users).order_by("created_at")
	serialized = PostSerializer(posts, many=True)
	return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like(request, pk):
	post = generics.get_object_or_404(Post, pk=pk)
	user = request.user

	if Like.objects.filter(user=user, post=post).exists():
		return Response({"info": "Already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

	like, created = Like.objects.get_or_create(user=user, post=post)
	notification = Notification.objects.create(
		recipient=post.author,
		actor=user,
		verb="liked your post",
		target=post,
		target_content_type=ContentType.objects.get_for_model(Post),
		target_object_id=post.id
	)

	return Response({"info": "Post liked."}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike(request, pk):
	post = generics.get_object_or_404(Post, pk=pk)
	user = request.user
	like = Like.objects.get(post=post)
	like.delete()
	return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
