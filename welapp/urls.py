from django.contrib import admin
from django.urls import path
from .views import welfunc, createList

urlpatterns = [
    path('list/', welfunc, name='list'),
    path('creat/', createList.as_view(), {})
]