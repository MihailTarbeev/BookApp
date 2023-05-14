from django import template
from django.db.models import Count
from BookApp.models import Author

register = template.Library()


@register.inclusion_tag('BookApp/authors_tpl.html')
def show_authors():
    authors = Author.objects.annotate(cnt=Count('readbooks')).filter(cnt__gt=0).order_by('-cnt')
    return {'authors': authors}
