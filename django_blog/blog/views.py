from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CreateUser
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Register(CreateView):
	model = User
	form_class = CreateUser
	template_name = "blog/register.html"
	success_url = reverse_lazy("login")

class Profile(LoginRequiredMixin, UpdateView):
	model = User
	fields = ["username", "first_name", "last_name", "email"]
	success_url = reverse_lazy("profile")
	template_name = "blog/profile.html"

	def get_object(self, queryset=None):
		return self.request.user