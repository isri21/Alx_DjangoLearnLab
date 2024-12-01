from rest_framework import serializers
from .models import Book, Author
from datetime import date

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"

	def validate_publication_year(self, value):
		if value > 2024:
			raise serializers.ValidationError("The Date Provided Is In The Future!")
		return value

class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer()
	class Meta:
		model = Author
		fields = "__all__"