from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Post
from .forms import CreateUser, UpdateUserForm, CreateForm
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Register(CreateView):
	model = User
	form_class = CreateUser
	template_name = "blog/register.html"
	success_url = reverse_lazy("login")

def profile(request):
	user = request.user
	if request.method == "POST":
		form = UpdateUserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect("profile")
		else:
			return render(request, "blog/profile.html", {"form": form})
	
	form = UpdateUserForm(instance=user)
	return render(request, "blog/profile.html", {"form": form})

class List(ListView):
	model = Post
	template_name = "list.html"
	context_object_name = "posts"
	template_name = "blog/list.html"

class Detail(DetailView):
	model = Post
	template_name = "list.html"
	context_object_name = "post"
	template_name = "blog/detail.html"

class New(CreateView):
	model = Post
	form_class = CreateForm
	template_name = "blog/create.html"
	success_url = reverse_lazy('posts')