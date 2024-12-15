from django.urls import path
from .views import register, login, profile, Follow, UnFollow
urlpatterns = [
	path("register/", register, name="register"),
	path("login/", login, name="login"),
	path("profile/", profile, name="profile"),
	path("follow/<int:user_id>/", Follow.as_view, name="follow"),
	path("unfollow/<int:user_id>/", UnFollow.as_view, name="unfollow"),
]