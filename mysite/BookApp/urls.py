from django.contrib import admin
from django.urls import path
from .views import Index, BooksByCategory


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<str:slug>/', BooksByCategory.as_view(), name='category')
]
