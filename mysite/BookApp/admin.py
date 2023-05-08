from django.contrib import admin
from .models import *


class ReadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'author', 'slug', 'category', 'date_of_reading', 'year_of_reading',
                    'feedback', 'estimation')
    list_display_links = ('id', 'title')


class UnreadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'author', 'category')
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


admin.site.register(ReadBooks, ReadBooksAdmin)
admin.site.register(UnreadBooks, UnreadBooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Year)

