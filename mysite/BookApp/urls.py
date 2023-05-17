from django.contrib import admin
from django.urls import path
from .views import Index, BooksByCategory, SingleBook, BooksByAuthor, FutureBooks, AddReadBooks, register, user_login, \
    user_logout

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<str:slug>/', BooksByCategory.as_view(), name='category'),
    path('book/<str:slug>/', SingleBook.as_view(), name='book'),
    path('author/<str:slug>/', BooksByAuthor.as_view(), name='author'),
    path('unreadbooks/', FutureBooks.as_view(), name='unreadbooks'),
    path('add_read_books/', AddReadBooks.as_view(), name='add_read_books'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
