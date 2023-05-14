from django.contrib import admin
from django.urls import path
from .views import Index, BooksByCategory, SingleBook, BooksByAuthor


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<str:slug>/', BooksByCategory.as_view(), name='category'),
    path('book/<str:slug>/', SingleBook.as_view(), name='book'),
    path('author/<str:slug>/', BooksByAuthor.as_view(), name='author'),
]
