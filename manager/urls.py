from django.urls import path

from manager.views import hello, world

urlpatterns = [
    path('hello/', hello),
    path('world/', world),
]