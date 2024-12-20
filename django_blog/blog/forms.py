from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django import forms
from taggit.forms import TagWidget

class CreateUser(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]

class CreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ["title", "content", "author", "tags"]
		widgets = {
			'tags': TagWidget()  # Use the TagWidget for a more interactive input field
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ["content"]