from django import template
from BookApp.models import ReadBooks

register = template.Library()


@register.inclusion_tag('BookApp/years_tpl.html', takes_context=True)
def show_years(context):
    request = context['request']
    years = []
    for obj in ReadBooks.objects.filter(user=request.user).values_list('date_of_reading', flat=True)\
            .order_by('-date_of_reading'):
        year = obj.year
        if year not in years:
            years.append(year)
    return {'years': years}

