from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})