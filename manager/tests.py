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
        self.client.force_login(self.user)
        self.book1 = Book.objects.create(title1="test_title1")
        self.book1.author.add(self.user)
        self.book1.save()
        self.book2 = Book.objects.create(title2="test_title2")
        self.assertEqual(Book.objects.count(), 2)
        data = {
            "title": "test_title2",
            "text": "test text"
        }
        url = reverse('update-book', kwargs=dict(slug=self.book1.slug))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, data['title'], msg="book1 is not refreshed")
        self.assertEqual(self.book1.text, data['text'], msg="book1 is not refreshed")
        self.assertEqual(self.book1.authors.firsr, self.user)
        self.client.logout()
        url = reverse('update-book', kwargs=dict(slug=self.book2.slug))
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, data['title'])
        self.assertEqual(self.book2.text, data['text'])


