from django import template

register = template.Library()


@register.filter
def equals(val, arg):
    return str(val) == str(arg)
