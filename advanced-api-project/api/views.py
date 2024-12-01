from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework

# Create your views here.
class ListView(generics.ListAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = "__all__"
	search_fields = ["title", "publication_year"]
	ordeing_fields = ["title", "publication_year"]

class DetailView(generics.RetrieveAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Book.objects.all()
	serializer_class = BookSerializer