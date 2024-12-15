from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
comment_router = DefaultRouter()
comment_router.register(r'comments', CommentViewSet)
from .views import feed, like, unlike

urlpatterns = [
	path('post/', include(post_router.urls)),
	path('comment/', include(comment_router.urls)),
	path('feed/', feed, name="feed"),
	path('posts/<int:pk>/like/', like, name='like'),
	path('posts/<int:pk>/unlike/', unlike, name='unlike'),
]
