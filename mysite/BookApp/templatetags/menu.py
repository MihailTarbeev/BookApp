from django import template
from django.db.models import Count, Q
from BookApp.models import Category

register = template.Library()


@register.inclusion_tag('BookApp/menu_tpl.html', takes_context=True)
def show_menu(context):
    request = context['request']
    categories = Category.objects.annotate(cnt=Count('readbooks', filter=Q(readbooks__user=request.user)))\
        .filter(cnt__gt=0).order_by('-cnt', 'title',)
    return {'categories': categories}
