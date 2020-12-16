from django.forms import ModelForm, TextInput, Textarea
from manager.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text"]
        widgets = {
        #     "title": TextInput(attrs={"class": "form-control"}),
        #     "text": Textarea(attrs={"class": "form-control", "rows"=5, "cols"=50})
        # }
        # help_texts = {
        #     "title",
        #     "text"
        # }

