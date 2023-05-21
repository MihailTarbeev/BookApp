from django import template
from django.db.models import Count, Q
from BookApp.models import Author

register = template.Library()


@register.inclusion_tag('BookApp/authors_tpl.html', takes_context=True)
def show_authors(context):
    request = context['request']
    authors = Author.objects.annotate(cnt=Count('readbooks', filter=Q(readbooks__user=request.user)))\
        .filter(cnt__gt=0).order_by('-cnt', 'name',)
    return {'authors': authors}
