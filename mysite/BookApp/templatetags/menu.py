from django import template
from django.db.models import Count

from BookApp.models import Category

register = template.Library()


@register.inclusion_tag('BookApp/menu_tpl.html')
def show_menu():
    categories = Category.objects.annotate(cnt=Count('readbooks')).filter(cnt__gt=0).order_by('-cnt', 'title',)
    return {'categories': categories}
