from django.contrib import admin
from .models import *


class ReadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'author', 'category', 'date_of_reading',
                    'estimation')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')


class UnreadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


admin.site.register(ReadBooks, ReadBooksAdmin)
admin.site.register(UnreadBooks, UnreadBooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
