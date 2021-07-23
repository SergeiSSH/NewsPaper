from django import template

register = template.Library()


@register.filter
def censor(bad):
    wordfilter_list = [
        'Fuck', 'FUCK'
    ]

    for c in wordfilter_list:
        bad = bad.replace(c, '***')
    return bad
