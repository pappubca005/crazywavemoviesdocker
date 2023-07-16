from django import template

register = template.Library()
# register.filter("remove_forward_slashes", remove_forward_slashes)


@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "/")
