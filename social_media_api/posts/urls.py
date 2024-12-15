from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

post_router = DefaultRouter()
post_router.register(r'posts', PostViewSet)
comment_router = DefaultRouter()
comment_router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(post_router.urls)),
    path('comments/', include(comment_router.urls)),
]
