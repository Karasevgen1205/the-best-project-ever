from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")

def world(request):
    return HttpResponse("Fuck off, world")

# Create your views here.
