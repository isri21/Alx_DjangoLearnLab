from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class Library(models.Model):
	name = models.CharField(max_length=100)
	books = models.ManyToManyField(Book)

	def __str__(self):
		return self.name

class Librarian(models.Model):
	name = models.CharField(max_length=150)
	library = models.OneToOneField(Library, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def str(self):
        return self.user.username
