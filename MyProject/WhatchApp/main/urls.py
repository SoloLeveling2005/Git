from django.urls import path,include
from .views import hi, index, build_index


urlpatterns = [
    path('',hi),
    path('index', index),
    path('build_index', build_index)
]