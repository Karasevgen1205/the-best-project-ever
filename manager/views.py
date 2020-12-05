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
        context = {'books': Book.objects.all()}
        #context['arr'] = ['igor', 'oleg', 'Abdyl', 'Rashid']
        return render(request, "index.html", context)

class AddLike(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            try:
                LikeBookUser.objects.create(user=request.user, book_id=id)
            except:
                LikeBookUser.objects.get(user=request.user, book_id=id).delete()
        return redirect("the-main-page")
