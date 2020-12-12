from django.core.management.base import BaseCommand
from slugify import slugify
from manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.all()
        for b in books:
           b.slug = slugify(b.title)
        Book.objects.bulk_update(books, ['slug'])

