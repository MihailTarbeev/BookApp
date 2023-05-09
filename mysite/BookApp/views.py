from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ReadBooks


class Index(ListView):
    model = ReadBooks
    template_name = 'BookApp/index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
