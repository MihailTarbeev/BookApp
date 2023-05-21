from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReadBooksAdminForm(forms.ModelForm):
    feedback = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Отзыв')

    class Meta:
        model = ReadBooks
        fields = '__all__'


class ReadBooksAdmin(admin.ModelAdmin):
    form = ReadBooksAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'author', 'category', 'date_of_reading',
                    'estimation', 'get_photo', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')
    fields = ('title', 'slug', 'author', 'category', 'date_of_reading', 'feedback', 'estimation', 'photo')

    # Функция позволит нам автоматически заполнять поле user админом
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Обложка'

    # Функция не позволяет нам создать объекты с автором, которого создал иной пользователь
    def get_form(self, request, obj=None, **kwargs):
        form = super(ReadBooksAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = Author.objects.filter(user=request.user)
        return form


class UnreadBooksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'author', 'category', 'get_photo', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'author')
    fields = ('title', 'slug', 'author', 'category')

    # Функция позволит нам автоматически заполнять поле user админом
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return "-"

    get_photo.short_description = 'Обложка'

    # Функция позволит нам автоматически заполнять поле user админом
    def get_form(self, request, obj=None, **kwargs):
        form = super(UnreadBooksAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].queryset = Author.objects.filter(user=request.user)
        return form


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('id', 'name', 'slug', 'user')
    list_display_links = ('id', 'name')

    # Функция позволит нам автоматически заполнять поле user админом
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(ReadBooks, ReadBooksAdmin)
admin.site.register(UnreadBooks, UnreadBooksAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
