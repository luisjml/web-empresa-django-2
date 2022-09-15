from django import template
from pages.models import Page

# register tiene la libreria de templates
register = template.Library()

# Registro mi tag en la libreria de templates
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages