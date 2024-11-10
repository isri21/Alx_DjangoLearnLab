from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView

urlpatterns = [
    path('', list_book),
    path('library-detail', LibraryDetailView.as_view()),
    path('login/', LoginView.as_view(template_name="users/login.html")),
    path('logout/', LogoutView.as_view(template_name="users/logout.html")),
    path('register/', views.register, name='register'),
]
