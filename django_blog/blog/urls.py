from django.urls import path
from .views import Register, Profile
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path("home/", Register.as_view(), name="home"),
	path("posts/", Register.as_view(), name="posts"),
	path("login/", LoginView.as_view(), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path("register/", Register.as_view(), name="register"),
	path("profile/", Profile.as_view(), name="profile"),
]