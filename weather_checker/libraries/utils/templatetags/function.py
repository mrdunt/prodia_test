from django import template

register = template.Library()


@register.filter(name='price')
def nominal_price(value):
    if value:
        price = '{:,.0f}'.format(value)
        return f'Rp{price}'
