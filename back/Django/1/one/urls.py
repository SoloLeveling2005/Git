from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index, build

urlpatterns = [
    path('', index),
    path('hi', build),
]
