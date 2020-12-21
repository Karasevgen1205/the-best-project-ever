from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Count, Prefetch, Exists, OuterRef
from django.shortcuts import render, redirect
from django.views import View
from manager.forms import BookForm, CustomAuthenticationForm, CommentForm
from manager.models import Book, LikeComment, Comment
from manager.models import LikeBookUser as RateBookUser
from django.contrib.auth.forms import AuthenticationForm


class MyPage(View):
    def get(self, request):
        context = {}
        books = Book.objects.prefetch_related("authors")
        if request.user.is_authenticated:
            is_owner = Exists(User.objects.filter(books =OuterRef("pk"), id = request.user.id))
            books = books.annotate(is_owner = is_owner)
        context['books'] = books
        context['range'] = range(1, 6)
        context['form'] = BookForm()
        return render(request, "index.html", context)

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {'form': CustomAuthenticationForm()})

    def post(self, request):
        user = CustomAuthenticationForm(data=request.POST)
        if user.is_valid():
            login(request, user.get_user())
        return redirect("the-main-page")


def logout_user(request):
    logout(request)
    return redirect("the-main-page")

class AddCommentLike(View):
    def get(self, request, slug, location=None):
        if request.user.is_authenticated:
            #com_id = Comment.objects.get(book__slug=slug).id
            LikeComment.objects.create(user=request.user, comment_id=slug)
        if location is None:
            return redirect("the-main-page")
        else:
            return redirect('book-detail', slug=slug)

class AddRate2Book(View):
    def get(self, request, slug, rate, location=None):
        if request.user.is_authenticated:
            #book_id = Book.objects.get(slug=slug).id
            RateBookUser.objects.create(user=request.user, book_id=slug, rate=rate)
        if location is None:
            return redirect("the-main-page")
        return redirect('book-detail', slug=slug)


class BookDetail(View):
    def get(self, request, slug):
        comment_query = Comment.objects.annotate(count_like=Count("likes_com")).select_related("author")
        comments = Prefetch("comments", comment_query)
        book = Book.objects.prefetch_related("authors", comments).get(slug=slug)
        return render(request, "book_detail.html", {"book": book, "rate": [1, 2, 3, 4, 5], "form": CommentForm()})

class AddBook(View):
    def post(self, request):
        if request.user.is_authenticated:
            bf = BookForm(data=request.POST)
            book = bf.save(commit=True)
            book.authors.add(request.user)
            book.save()
        return redirect("the-main-page")

class AddComment(View):
    def post(self, request, slug):
        if request.user.is_authenticated:
            # Comment.objects.create(book_id=id, text=request.POST.get('text'), author_id=request.user.id)
            cf = CommentForm(data=request.POST)
            comment = cf.save(commit=False)
            comment.author_id = request.user.id
            comment.book_id = slug
            comment.save()
        return redirect("book-detail", slug=slug)

def book_delete(request, slug):
    if request.user.is_authenticated:
        book = Book.objects.get(slug=slug)
        if request.user in book.authors.all():
            book.delete()
    return redirect('the-main-page')

class UpdateBook(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            book = Book.objects.get(slug=slug)
            if request.user in book.authors.all():
                form = BookForm(instance=book)
                return render(request, "update_book.html", {"form":form, "slug":book.slug})
        return redirect('the-main-page')

    def post(self, request, slug):
        if request.user.is_authenticated:
            book = Book.objects.get(slug=slug)
            if request.user in book.authors.all():
                bf = BookForm(instance=book, date = request.POST)
                if bf.is_valid():
                    bf.save(commit=True)
        return redirect('the-main-page')
