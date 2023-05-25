from django import template
from django.db.models import Count, Q
from BookApp.models import Category
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag('BookApp/menu_tpl.html', takes_context=True)
def show_menu(context):
    categories = cache.get('categories')
    if not categories:
        request = context['request']
        categories = Category.objects.annotate(cnt=Count('readbooks', filter=Q(readbooks__user=request.user)))\
            .filter(cnt__gt=0).order_by('-cnt', 'title',)
        cache.set('categories', categories, 15)
    return {'categories': categories}
