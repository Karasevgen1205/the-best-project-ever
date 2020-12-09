from django.db.models import Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from manager.models import Book, Comment, LikeBookUser, LikeCommentUser


def hello(request, name='filipp', digit=None):
    if digit is not None:
        return HttpResponse(f"digit is {digit}")
    return HttpResponse(f"hello {name}")


# class MyPage(View):
#     def get(self, request):
#         context = {}
#         comment_query = Comment.objects.annotate(count_liked=Count('users_like'))
#         comments = Prefetch("comments", comment_query)
#         context['books'] = Book.objects.prefetch_related("authors", comments).\
#             annotate(coun_liket=Count('users_like'))
#         return render(request, "index.html", context)


class MyPage(View):
    def get(self, request):
        context = {}
        comment_query = Comment.objects.annotate(count_liked=Count('users_like')).select_related("author")
        comments = Prefetch("comments", comment_query)
        books = Book.objects.prefetch_related("authors", comments)
        context['books'] = books
        context['rate'] = "4"
        return render(request, "index.html", context)


class AddLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect("the-main-page")


class AddLike2Comment(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)
        return redirect("the-main-page")

class AddRate2Book(View):
    def get(self, request, id, rate):
        return redirect("the-main-page")

class BookDetail(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        return render(request, "book_detail.html", {'book': book, "raye": 2})
