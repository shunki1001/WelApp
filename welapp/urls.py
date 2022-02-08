from django.contrib import admin
from django.urls import path
from .views import welfunc, createList, detailView

urlpatterns = [
    path('list/', welfunc, name='list'),
    path('create/', createList.as_view(), name='create'),
    path('detail/<int:pk>', detailView.as_view(), name='detail'),
]