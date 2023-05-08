from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max
from django.utils.datetime_safe import date
from django.core.validators import MaxValueValidator, MinValueValidator


def get_max_year():
    return Year.objects.all().order_by("-title")[0]


class ReadBooks(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    author = models.CharField(max_length=50, verbose_name='Автор')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)
    date_of_reading = models.DateField(default=date.today, verbose_name='Дата прочтения')
    year_of_reading = models.ForeignKey('Year', verbose_name='Год прочтения', on_delete=models.PROTECT,
                                        default=get_max_year)
    feedback = models.TextField(verbose_name='Отзыв', blank=True)
    estimation = models.IntegerField(verbose_name='Оценка (от 0 до 10)', validators=[
        MaxValueValidator(10),
        MinValueValidator(0),
    ])
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь', default=User)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_of_reading']
        verbose_name = 'Прочитанная книга'
        verbose_name_plural = 'Прочитанные книги'


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Year(models.Model):
    title = models.CharField(max_length=4, verbose_name='Год')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'


class UnreadBooks(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)
    author = models.CharField(max_length=50, verbose_name='Автор')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь', default=User)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Непрочитанная книга'
        verbose_name_plural = 'Непрочитанные книги'
