from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from manager.models import Book


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
            #book = Book.objects.get(id=id)
            #book.likes += 1
            #book.save()
            book = Book.objects.get(id=id)
            book.likes.add(request.user)
            book.save()
            if request.user in book.likes.all():
                book.likes.filter(user_id=request.user.id).delete()
            else:
                book.likes.add(request.user)
                book.save()
        return redirect("the-main-page")
