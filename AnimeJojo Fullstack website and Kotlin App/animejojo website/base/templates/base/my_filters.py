from django.template import Library

register = Library()

@register.filter(name='loop')
def loop(a,b):
    # count = 0
    # while count < 14477:
    #     for i in range(14477):
    #         count += 1
    #         return count
    return range(14477)

@register.filter(name='index')
def index(a,b):
    return a[b]