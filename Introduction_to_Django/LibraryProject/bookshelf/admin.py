from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["author", "publication_year"]
