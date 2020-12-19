from django.core.management.base import BaseCommand
from manager.models import Book, TMPBook, LikeBookUser, Comment


class Commnd(BaseCommand):
    def hendle(self, *args, **options):
