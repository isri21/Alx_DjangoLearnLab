from django.urls import path
from relationship_app.views import list_book, LibraryDetail

urlpatterns = [
    path('', list_book),
    path('library-detail', LibraryDetail.as_view()),
]
