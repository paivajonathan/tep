from django import template
from datetime import date, time


register = template.Library()


@register.filter
def uppercaseify(value):
    value = str(value)
    return value.upper()


@register.filter
def readable_date(value):
    if not isinstance(value, date):
        return value
    
    day = str(value.day).zfill(2)
    month = str(value.month).zfill(2)

    return f'{day}/{month}'


@register.filter
def readable_time(value):
    if not isinstance(value, time):
        return value
    
    result = f'{value.hour}h'

    if value.minute != 0:
        result += f'{value.minute} min'

    return result