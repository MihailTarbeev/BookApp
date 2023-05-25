from django import forms
from datetime import date
import re
from django.core.exceptions import ValidationError
from .models import ReadBooks, Author, UnreadBooks
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReadBookForm(forms.ModelForm):
    feedback = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Отзыв')

    class Meta:
        model = ReadBooks
        exclude = ['user', 'slug']

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search(r'\d', title):
            raise ValidationError('Название не должно содержать цифры')
        return title

    # Запретим добавлять книги, у которых дата позже сегодняшней
    def clean_date_of_reading(self):
        date_of_reading = self.cleaned_data['date_of_reading']
        now = date.today()
        delta = now - date_of_reading
        if delta.total_seconds() < 0:
            raise ValidationError('Дата прочтения не может быть в будущем')
        return date_of_reading


class UserLoginFrom(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'login_field', 'style': 'width: 30%; margin: auto auto;'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'login_field', 'style': 'width: 30%; margin: auto auto;'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(), required=False,
                             help_text='Не обязательное поле')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.search(r'\d', name):
            raise ValidationError('Имя автора не должно содержать цифр')
        return name


class UnreadBookForm(forms.ModelForm):
    class Meta:
        model = UnreadBooks
        exclude = ['user', 'slug']

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.search(r'\d', title):
            raise ValidationError('Название не должно содержать цифры')
        return title


class DeleteReadBookForm(forms.ModelForm):
    class Meta:
        model = ReadBooks
        fields = []


class DeleteUnreadBookForm(forms.ModelForm):
    class Meta:
        model = UnreadBooks
        fields = []


class DeleteAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = []
