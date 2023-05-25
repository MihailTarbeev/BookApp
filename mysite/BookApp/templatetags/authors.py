from django import template
from django.db.models import Count, Q
from BookApp.models import Author
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag('BookApp/authors_tpl.html', takes_context=True)
def show_authors(context):
    authors = cache.get('authors')
    if not authors:
        request = context['request']
        authors = Author.objects.annotate(cnt=Count('readbooks', filter=Q(readbooks__user=request.user)))\
            .filter(cnt__gt=0).order_by('-cnt', 'name',)[:3]
        cache.set('authors', authors, 15)
    return {'authors': authors}
