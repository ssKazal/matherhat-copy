from django import template
from django.template.defaultfilters import stringfilter
from core.utils import NUMBER_MAP


register = template.Library()


@register.filter
@stringfilter
def translate_bangla_numeral(value):
    try:
        return "".join([NUMBER_MAP[char] for char in value])
    except KeyError:
        return value
