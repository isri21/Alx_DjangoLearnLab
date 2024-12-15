from django.urls import path
from .views import register, login, profile, follow, unfollow
urlpatterns = [
	path("register/", register, name="register"),
	path("login/", login, name="login"),
	path("profile/", profile, name="profile"),
	path("follow/<int:user_id>", follow, name="follow"),
	path("unfollow/<int:user_id>", unfollow, name="unfollow"),
]