from django.db.models import Count
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from .models import ReadBooks, Category, Author, UnreadBooks
from .forms import ReadBookForm
from pytils.translit import slugify
from django.contrib import messages
from django.contrib.auth import login, logout
from BookApp.forms import UserRegisterForm, UserLoginFrom, AuthorForm, UnreadBookForm, DeleteReadBookForm, \
    DeleteUnreadBookForm, DeleteAuthorForm


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

    def get_queryset(self):
        return ReadBooks.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cnt_all'] = ReadBooks.objects.filter(user=self.request.user).count()
        return context


class BooksByCategory(ListView):
    model = ReadBooks
    template_name = 'BookApp/category.html'
    context_object_name = 'books'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return ReadBooks.objects.filter(category__slug=self.kwargs['slug'], user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.filter(user=self.request.user).count()
        context['cnt'] = ReadBooks.objects.filter(category__slug=self.kwargs['slug'], user=self.request.user).count()
        return context


class SingleBook(DetailView):
    model = ReadBooks
    template_name = 'BookApp/single.html'
    context_object_name = 'book'

    def get_queryset(self):
        return ReadBooks.objects.filter(slug=self.kwargs['slug'], user=self.request.user)

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
        return ReadBooks.objects.filter(author__slug=self.kwargs['slug'], user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Author.objects.get(slug=self.kwargs['slug'])
        context['cnt_all'] = ReadBooks.objects.filter(user=self.request.user).count()
        context['cnt'] = ReadBooks.objects.filter(author__slug=self.kwargs['slug'], user=self.request.user).count()
        return context


class FutureBooks(ListView):
    model = UnreadBooks
    template_name = 'BookApp/unreadbooks.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return UnreadBooks.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Книги на будущее'
        context['cnt_all'] = UnreadBooks.objects.filter(user=self.request.user).count()
        return context


class AddReadBooks(CreateView):
    form_class = ReadBookForm
    template_name = 'BookApp/add_readbook.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = original_slug = slugify(form.instance.title)
        i = 1
        while ReadBooks.objects.filter(slug=form.instance.slug):
            form.instance.slug = '{}-{}'.format(original_slug, i)
            i += 1
        return super(AddReadBooks, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление книги'
        context['cnt_all'] = ReadBooks.objects.count()
        return context


class AddAuthor(CreateView):
    form_class = AuthorForm
    template_name = 'BookApp/add_author.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = original_slug = slugify(form.instance.name)
        i = 1
        while Author.objects.filter(slug=form.instance.slug):
            form.instance.slug = '{}-{}'.format(original_slug, i)
            i += 1
        return super(AddAuthor, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление автора'
        context['cnt_all'] = ReadBooks.objects.count()
        return context


class AddUnreadBooks(CreateView):
    form_class = UnreadBookForm
    template_name = 'BookApp/add_unreadbook.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = original_slug = slugify(form.instance.title)
        i = 1
        while UnreadBooks.objects.filter(slug=form.instance.slug):
            form.instance.slug = '{}-{}'.format(original_slug, i)
            i += 1

        return super(AddUnreadBooks, self).form_valid(form)

    def get_success_url(self):
        return reverse('unreadbooks')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление книги'
        context['cnt_all'] = UnreadBooks.objects.count()
        return context


def delete_read_book(request, id):
    book_to_delete = get_object_or_404(ReadBooks, pk=id, user=request.user)
    if request.method == 'POST':
        form = DeleteReadBookForm(request.POST, instance=book_to_delete)
        if form.is_valid():
            book_to_delete.delete()
            messages.success(request, 'Книга была успешна удалена!')
            return redirect('/')
    else:
        form = DeleteReadBookForm(instance=book_to_delete)
    return render(request, 'BookApp/delete_read_book.html', {'form': form, 'book': book_to_delete})


def delete_unread_book(request, id):
    book_to_delete = get_object_or_404(UnreadBooks, pk=id, user=request.user)
    if request.method == 'POST':
        form = DeleteUnreadBookForm(request.POST, instance=book_to_delete)
        if form.is_valid():
            book_to_delete.delete()
            messages.success(request, 'Книга была успешна удалена!')
            return redirect('/')
    else:
        form = DeleteUnreadBookForm(instance=book_to_delete)
    return render(request, 'BookApp/delete_unread_book.html', {'form': form, 'book': book_to_delete})


class ListAuthors(ListView):
    model = Author
    template_name = 'BookApp/list_authors.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.annotate(cnt_r=Count('readbooks')).annotate(cnt_unr=Count('unreadbooks')).\
            filter(cnt_r=0, cnt_unr=0, user=self.request.user).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список авторов'
        context['cnt_all'] = ReadBooks.objects.count()
        return context


def delete_author(request, id):
    author_to_delete = get_object_or_404(Author, pk=id, user=request.user)
    if request.method == 'POST':
        form = DeleteAuthorForm(request.POST, instance=author_to_delete)
        if form.is_valid():
            author_to_delete.delete()
            messages.success(request, 'Автор был успешно удален!')
            return redirect('/')
    else:
        form = DeleteAuthorForm(instance=author_to_delete)
    return render(request, 'BookApp/delete_author.html', {'form': form, 'author': author_to_delete})
