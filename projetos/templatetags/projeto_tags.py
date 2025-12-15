from django import template

register = template.Library()

@register.filter
def split_tec(value):
    if not value:
        return []
    return [t.strip() for t in value.split(',') if t.strip()]
