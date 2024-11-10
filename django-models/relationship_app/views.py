from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def list_books(request):
	books = Book.objects.all()
	context = {'books': books}

	return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    template_name = 'users/logout.html'

def check_role(user, role):
    return user.userprofile.role == role

@user_passes_test(lambda u: check_role(u, 'Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: check_role(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: check_role(u, 'Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
