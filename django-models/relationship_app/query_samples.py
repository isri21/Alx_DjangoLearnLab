from relationship_app.models import Author, Library, Librarian, Book
author = Author.objects.get(name=auhtor_name)
Book.objects.filter(author=author)
h = Library.objects.get(name=library_name)
h.books.all()
library = Library.objects.get(name=library_name)
Librarian.objects.get(library=library)
