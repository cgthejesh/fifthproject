from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello Amogh.</h1>"
                        "<br><h2>Our first and many more Heroku, Pycharm and Git website</h2>")
