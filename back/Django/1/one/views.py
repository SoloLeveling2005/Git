from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {

    }
    return render(request, 'one/index.html', context)


def build(request):
    context = {

    }
    return render(request, 'one/build.html', context)
