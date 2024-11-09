from relationship_app.models import Book, Library, Librarian
Book.objects.filter(author__name="author")
Library.objects.all()
Librarian.objects.get(library="")
