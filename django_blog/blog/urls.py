from django.urls import path
from .views import Register, profile
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("home/", Register.as_view(), name="home"),
	path("posts/", Register.as_view(), name="posts"),
	path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", Register.as_view(), name="register"),
	path("profile/", profile, name="profile"),
]