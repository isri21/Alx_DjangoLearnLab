from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        self.book1 = Book.objects.create(title="Django for Beginners", publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", publication_year=2021)
        self.client = APIClient()

    def test_create_book(self):
        data = {
            "title": "New Django Book",
            "publication_year": 2022
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        data = {"title": "Updated Title", "publication_year": 2020}
        response = self.client.put(f'/api/books/{self.book1.id}/', data)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 