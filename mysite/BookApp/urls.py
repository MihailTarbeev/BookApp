from django.contrib import admin
from django.urls import path
from .views import Index, BooksByCategory, SingleBook


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<str:slug>/', BooksByCategory.as_view(), name='category'),
    path('book/<str:slug>/', SingleBook.as_view(), name='book'),
]
