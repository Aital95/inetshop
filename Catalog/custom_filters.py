from django import template

register = template.Library()


@register.filter(name='mediapath')
def mediapath_filter(value):
    # Assuming value is a relative image path, convert it to a full media path
    return f'/media/{value}'
