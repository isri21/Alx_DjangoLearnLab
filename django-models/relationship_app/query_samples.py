from relationship_app.models import Author, Library, Librarian, Book
Book.objects.filter(author__name="")
Library.objects.all()
Librarian.objects.get(library="")