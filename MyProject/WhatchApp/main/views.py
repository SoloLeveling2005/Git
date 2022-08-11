from django.shortcuts import render
from django.http import HttpResponse


def hi(request):
    return HttpResponse("<a href='/index'>Перейти на страницу index</a>")


def index(request):
    content = {

    }
    return render(request, "main/index.html", content)



def build_index(request):
    content = {

    }
    return render(request, "build/build_index.html", content)