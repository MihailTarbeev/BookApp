from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReadBooksAdminForm(forms.ModelForm):
    feedback = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ReadBooks
        fields = '__all__'


class ReadBooksAdmin(admin.ModelAdmin):
    form = ReadBooksAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'author', 'category', 'date_of_reading',
                    'estimation', 'get_photo',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Обложка'


class UnreadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'author', 'category', 'get_photo',)
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Обложка'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')


admin.site.register(ReadBooks, ReadBooksAdmin)
admin.site.register(UnreadBooks, UnreadBooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
