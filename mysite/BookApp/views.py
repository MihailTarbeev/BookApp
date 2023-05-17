from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from .models import ReadBooks, Category, Author, UnreadBooks
from .forms import ReadBookForm
from pytils.translit import slugify
from django.contrib import messages
from django.contrib.auth import login, logout
from BookApp.forms import UserRegisterForm, UserLoginFrom


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'BookApp/register.html', {'form': form, 'title': 'Регистрация'})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLoginFrom()
    return render(request, 'BookApp/login.html', context={'form': form, 'title': 'Авторизация'})


def user_logout(request):
    logout(request)
    return redirect('login')


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

    def get_queryset(self):
        return ReadBooks.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BooksByAuthor(ListView):
    model = ReadBooks
    template_name = 'BookApp/author.html'
    context_object_name = 'books'
    allow_empty = True
    paginate_by = 5

    def get_queryset(self):
        return ReadBooks.objects.filter(author__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Author.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.count()
        context['cnt'] = ReadBooks.objects.filter(author__slug=self.kwargs['slug']).count()
        return context


class FutureBooks(ListView):
    model = UnreadBooks
    template_name = 'BookApp/unreadbooks.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги на будущее'
        context['cnt_all'] = UnreadBooks.objects.count()
        return context


class AddReadBooks(CreateView):
    form_class = ReadBookForm
    template_name = 'BookApp/add_readbook.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super(AddReadBooks, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление книги'
        context['cnt_all'] = ReadBooks.objects.count()
        return context
