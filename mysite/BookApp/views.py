from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import ReadBooks, Category, Author


class Index(ListView):
    model = ReadBooks
    template_name = 'BookApp/index.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cnt_all'] = ReadBooks.objects.count()
        return context


class BooksByCategory(ListView):
    model = ReadBooks
    template_name = 'BookApp/category.html'
    context_object_name = 'books'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return ReadBooks.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.count()
        context['cnt'] = ReadBooks.objects.filter(category__slug=self.kwargs['slug']).count()
        return context


class SingleBook(DetailView):
    model = ReadBooks
    template_name = 'BookApp/single.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BooksByAuthor(ListView):
    model = ReadBooks
    template_name = 'BookApp/author.html'
    context_object_name = 'books'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return ReadBooks.objects.filter(author__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Author.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.count()
        context['cnt'] = ReadBooks.objects.filter(author__slug=self.kwargs['slug']).count()
        return context
