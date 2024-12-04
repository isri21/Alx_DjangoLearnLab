from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms

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
		fields = ["title", "content", "author"]