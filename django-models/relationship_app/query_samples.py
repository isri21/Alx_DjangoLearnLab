from relationship_app.models import Author, Library, Librarian, Book
Book.objects.filter(author__name=auhtor_name)
h = Library.objects.get(name=library_name)
h.books.all()
Librarian.objects.get(library=library_name)