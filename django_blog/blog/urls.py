from django.urls import path
from .views import (
	Register, profile, List, Detail, 
	New, Edit, Delete, CommentCreateView, 
	CommentUpdateView, CommentDeleteView, search, tags
	)
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("home/", Register.as_view(), name="home"),
	path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", Register.as_view(), name="register"),
	path("profile/", profile, name="profile"),
	path("posts/", List.as_view(), name="posts"),
	path("posts/<int:pk>", Detail.as_view(), name="post-detail"),
	path("post/new/", New.as_view(), name="new"),
	path("post/<int:pk>/update/", Edit.as_view(), name="edit_post"),
	path("post/<int:pk>/delete/", Delete.as_view(), name="delete_post"),
	path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_post"),
	path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="edit_comment"),
	path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete_comment"),
	path("search/", search, name="search"),
	path("tags/<tag_name>/", tags, name="tags")
]