from django import forms
from .models import ReadBooks
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ReadBookForm(forms.ModelForm):
    class Meta:
        model = ReadBooks
        # fields = ['title', 'slug', 'author', 'category', 'date_of_reading', 'feedback', 'estimation', 'photo', 'user']
        # fields = '__all__'
        exclude = ['user', 'slug']


class UserLoginFrom(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
