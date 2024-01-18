# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='isdigit')
def isdigit(value):
    return str(value).isdigit()
