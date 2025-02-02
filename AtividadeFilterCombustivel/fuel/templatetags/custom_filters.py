from django import template


register = template.Library()


@register.filter
def moneyify(value):
    value = str(value).replace('.', ',')
    return f'R$ {value}'


@register.filter
def kilometerify(value):
    value = str(value).replace('.', ',')
    return f'{value} Km'
