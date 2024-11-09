from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library

# Create your views here.
def list_book(request):
	books = Book.objects.all()
	context = {'books': books}

	return render(request, 'relationship_app/list_books.html', context)

class LibraryDetail(ListView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'