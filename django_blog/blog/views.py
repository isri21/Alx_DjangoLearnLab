from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import CreateUser, UpdateForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Register(CreateView):
	model = User
	form_class = CreateUser
	template_name = "blog/register.html"
	success_url = reverse_lazy("login")

# class Profile(LoginRequiredMixin, UpdateView):
# 	model = User
# 	fields = ["username", "first_name", "last_name", "email"]
# 	success_url = reverse_lazy("profile")
# 	template_name = "blog/profile.html"

# 	def get_object(self, queryset=None):
# 		return self.request.user

def profile(request):
	user = request.user
	if request.method == "POST":
		form = UpdateForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect("profile")
		else:
			return render(request, "blog/profile.html", {"form": form})
	
	form = UpdateForm(instance=user)
	return render(request, "blog/profile.html", {"form": form})