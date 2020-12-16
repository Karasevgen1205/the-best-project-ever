from django.forms import ModelForm
from manager.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text"]
