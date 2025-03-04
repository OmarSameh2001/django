from django import template

register = template.Library()

@register.filter
def filter_by_name(schools, search):
    if not search:
        return schools
    search = search.lower()
    return [school for school in schools if search in school.name.lower()]
