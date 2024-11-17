from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView, admin_view, librarian_view, member_view, edit_book, add_book, delete_book

urlpatterns = [
    path('', list_book),
    path('library-detail', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name="users/login.html")),
    path('logout/', LogoutView.as_view(template_name="users/logout.html")),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'), 
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add/', add_book, name='add_book/'),
    path('edit/<int:pk>/', edit_book, name='edit_book/'),
    path('delete/<int:pk>/', delete_book, name='delete_book/'),
]
