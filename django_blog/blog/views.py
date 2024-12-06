from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CreateUser, UpdateUserForm, CreateForm, CommentForm
from django.views.generic import View, CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
class Register(CreateView):
	model = User
	form_class = CreateUser
	template_name = "blog/register.html"
	success_url = reverse_lazy("login")

@login_required
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
	context_object_name = "posts"
	# template_name = "blog/list.html"

class Detail(DetailView):
	model = Post
	context_object_name = "post"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["comments"] = Comment.objects.filter(post=self.object)

		return context
	
class New(LoginRequiredMixin, CreateView):
	model = Post
	form_class = CreateForm
	# template_name = "blog/create.html"
	success_url = reverse_lazy('posts')

class Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = CreateForm
	template_name = "blog/edit.html"
	success_url = reverse_lazy('posts')
	context_object_name = "post"

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author

class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	# template_name = "blog/delete.html"
	success_url = reverse_lazy('posts')
	context_object_name = "post"

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.author
	
# @login_required
# def add_comment(request, post_id):
# 	post = get_object_or_404(Post, id=post_id)
# 	if request.method == "POST":
		

class CommentCreateView(LoginRequiredMixin, View):
	def get(self, request, pk):
		post = get_object_or_404(Post, id=pk)
		form = CommentForm()
		return render(request, "blog/comment_post.html", {"post": post,	"form": form})
	
	def post(self, request, pk):
		post = get_object_or_404(Post, id=pk)
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post = post
			comment.save()
			return redirect("post-detail", pk=pk)
		else:
			return render(request, "blog/comment_post.html", {"post": post,	"form": form})
	
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
	def test_func(self):
		comment_id = self.kwargs['pk']
		comment = get_object_or_404(Comment, id=comment_id)
		return self.request.user == comment.author
	def get(self, request, pk):
		comment = get_object_or_404(Comment, id=pk)
		form = CommentForm(instance=comment)
		return render(request, "blog/comment_update.html", {"form": form, "comment": comment})
	def post(self, request, pk):
		comment = get_object_or_404(Comment, id=pk)
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			form.save()
			return redirect("posts")
		else:
			return render(request, "blog/comment_update.html", {"form": form, "comment": comment})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
	def test_func(self):
		comment_id = self.kwargs["pk"]
		comment = get_object_or_404(Comment, id=comment_id)
		return self.request.user == comment.author
	
	def get(self, request, pk):
		comment = get_object_or_404(Comment, id=pk)
		return render(request, "blog/comment_confirm_delete.html", {"comment": comment})
	
	def post(self, request, pk):
		comment = get_object_or_404(Comment, id=pk)
		comment.delete()
		comment.save()
		return redirect("posts")

def search(request):
	key = request.GET.get("search", None)
	if key == None:
		posts = []
	else:
		posts = Post.objects.filter(
			Q(title__icontains = key) | Q(content__icontains = key) | Q(tags__name__icontains = key) | Q(author__username__icontains = key)
		).distinct()
	return render(request, "blog/search.html", {"posts": posts})

def tags(request, tag_name):
	posts = Post.objects.filter(tags__slug__icontains = tag_name)
	context = {
		"posts": posts,
		"tag": tag_name
	}
	return render(request, "blog/taglist.html", context)
	