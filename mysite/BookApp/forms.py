from django import forms
from .models import ReadBooks, Author
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ReadBookForm(forms.ModelForm):
    feedback = forms.CharField(widget=CKEditorUploadingWidget(), required=False, label='Отзыв')

    class Meta:
        model = ReadBooks
        # fields = ['title', 'slug', 'author', 'category', 'date_of_reading', 'feedback', 'estimation', 'photo', 'user']
        # fields = '__all__'
        exclude = ['user', 'slug']


class UserLoginFrom(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
