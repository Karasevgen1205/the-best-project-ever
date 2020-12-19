from django.core.management.base import BaseCommand
from manager.models import Book, TMPBook, LikeBookUser, Comment


class Commnd(BaseCommand):
    def hendle(self, *args, **options):
        books = Book.objects.all()
        arr = [
            TMPBook(
                title=b.title,
                text=b.text,
                date=b.date,
                rate=b.rate,
                count_rated_users=b.count_rated_users,
                count_all_stars=b.count_all_stars,
                slug=b.slug
            )
            for b in books
        ]
        TMPBook.objects.bulk_create(arr)
        print('done')
        query = Book.objects.all().values("slug", "id")
        all_lbu=LikeBookUser.objects.all()
        for book in query:
            pass

