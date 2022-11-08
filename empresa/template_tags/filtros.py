from django import template

register = template.Library()

@register.filter(name="is_par")
def in_par(valor):
    #if ternario em Python
    return True if valor % 2 == 0 else False