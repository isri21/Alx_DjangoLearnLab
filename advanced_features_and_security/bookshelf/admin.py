from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ["author", "publication_year"]
    search_fields = ["title", "author", "publication_year"]

@admin.register(CustomUser)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "date_of_birth")
