from django.contrib import admin
from django.urls import path
from .views import welfunc, createList

urlpatterns = [
    path('list/', welfunc, name='list'),
    path('create/', createList.as_view(), name='create')
]