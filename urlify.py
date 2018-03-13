import urllib.parse as urllib_parse
from django import template

register = template.Library()


@register.filter
def urlify(value):
    return urllib_parse.quote_plus(value)
