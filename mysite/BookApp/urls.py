from django.contrib import admin
from django.urls import path
from .views import Index, BooksByCategory, SingleBook, BooksByAuthor, FutureBooks, AddReadBooks, register, user_login, \
    user_logout, AddAuthor, AddUnreadBooks, delete_read_book, delete_unread_book, ListAuthors, delete_author

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
    path('add_author/', AddAuthor.as_view(), name='add_author'),
    path('add_unread_books/', AddUnreadBooks.as_view(), name='add_unread_book'),
    path('delete_read_book/<int:id>/', delete_read_book, name='delete_read_book'),
    path('delete_unread_book/<int:id>/', delete_unread_book, name='delete_unread_book'),
    path('list_authors/', ListAuthors.as_view(), name='list_authors'),
    path('delete_author/<int:id>/', delete_author, name='delete_author'),
]
