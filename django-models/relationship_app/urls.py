from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView, admin_view, librarian_view, member_view

urlpatterns = [
    path('', list_book),
    path('library-detail', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name="users/login.html")),
    path('logout/', LogoutView.as_view(template_name="users/logout.html")),
    path('register/', views.register, name='register'),
    path('admin-view/', admin_view, name='admin_view'), 
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
