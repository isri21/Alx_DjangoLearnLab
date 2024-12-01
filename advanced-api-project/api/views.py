from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class ListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
	permission_classes = [permissions.IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer