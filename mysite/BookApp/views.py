from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ReadBooks, Category


class Index(ListView):
    model = ReadBooks
    template_name = 'BookApp/index.html'
    context_object_name = 'books'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cnt'] = ReadBooks.objects.count()
        return context


class BooksByCategory(ListView):
    model = ReadBooks
    template_name = 'BookApp/category.html'
    context_object_name = 'books'
    allow_empty = False
    paginate_by = 4

    def get_queryset(self):
        return ReadBooks.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.count()
        context['cnt'] = ReadBooks.objects.filter(category__slug=self.kwargs['slug']).count()
        return context

# class PostsByCategory(ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'posts'
#     paginate_by = 4
#     # При запросе пустой категории выдаст ошибку
#     allow_empty = False
#
#     def get_queryset(self):
#         return Post.objects.filter(category__slug=self.kwargs['slug'])
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = Category.objects.get(slug=self.kwargs['slug'])
#         return context