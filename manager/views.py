from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from manager.models import Book, LikeBookUser


def hello(request, name='filipp', digit=None):
    if digit is not None:
        return HttpResponse(f"digit is {digit}")
    return HttpResponse(f"hello {name}")


class MyPage (View):
    def get(self, request):
        #context = {}
        context = {'books': Book.objects.prefetch_related('authors')}
        #context['arr'] = ['igor', 'oleg', 'Abdyl', 'Rashid']
        return render(request, "index.html", context)


class AddLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
           LikeBookUser.objects.create(user=request.user, book_id=id)
        return redirect("the-main-page")
