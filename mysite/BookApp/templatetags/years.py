from django import template
from BookApp.models import ReadBooks
from django.core.cache import cache

register = template.Library()


@register.inclusion_tag('BookApp/years_tpl.html', takes_context=True)
def show_years(context):
    years = cache.get('years')
    if not years:
        request = context['request']
        years = []
        for obj in ReadBooks.objects.filter(user=request.user).values_list('date_of_reading', flat=True)\
                .order_by('-date_of_reading'):
            year = obj.year
            if year not in years:
                years.append(year)
        cache.set('years', years, 15)
    return {'years': years}

