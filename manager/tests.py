from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from slugify import slugify
from manager.models import Book


class TestMyAppPlease(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("test_name")

    def test_add_book(self):
        self.client.force_login(self.user)
        url = reverse("add-book")
        data = {
            "title": "test_title",
            "text": "test text"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg="is not redirect")
        self.assertEqual(Book.objects.exists(), msg="book is not created")
        book = Book.objects.first()
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.title, data['title'])
        self.assertEqual(book.slug, slugify(data['title']))
        self.assertEqual(book.authors.first(), self.user)
        self.client.logout()
        data = {
            "title": "test_title2",
            "text": "test text"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302, msg="is not redirect")
        self.assertEqual(Book.objects.count(), 1, msg="created book whithout author")

    def test_update_book(self):
        book1 = Book(title1="test_title1")
        book2 = Book(title2="test_title2")
        book3 = Book(title3="test_title3")
        Book.objects.bulk_create([book1, book2, book3])
        self.assertEqual(Book.object.count(), 3)

