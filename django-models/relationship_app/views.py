from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book 

# Create your views here.
def list_book(request):
	books = Book.objects.all()
	context = {'books': books}

	return render(request, 'relationship_app/list_books.html', context)

class LibraryDetail(DetailView):
	model = Library
	template_name = 'relationship_app/library_detail.html'
	context_object_name = 'library'