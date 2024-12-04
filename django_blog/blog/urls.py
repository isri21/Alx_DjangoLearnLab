from django.urls import path
from .views import Register, profile, List, Detail, New
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("home/", Register.as_view(), name="home"),
	path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", Register.as_view(), name="register"),
	path("profile/", profile, name="profile"),
	path("posts/", List.as_view(), name="posts"),
	path("posts/<int:pk>", Detail.as_view(), name="post-detail"),
	path("posts/new/", New.as_view(), name="new"),
]