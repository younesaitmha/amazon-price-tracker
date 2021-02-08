from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def colorize(value):
    mark = str(value)[:1]
    if mark == "-":
        html_str = f"<span style='color:green'>${value}</span>"
    elif value == 0:
        html_str = f"<span style='color:blue'>${value}</span>"
    else:
        html_str = f"<span style='color:red'>${value}</span>"
    return mark_safe(html_str)
