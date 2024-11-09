from django.urls import path
from .views import list_book, LibraryDetailView

urlpatterns = [
    path('', list_book),
    path('library-detail', LibraryDetailView.as_view()),
]
