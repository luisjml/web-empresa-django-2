from .models import Link

# Context dictionary, diccionariod e contexto
def ctx_dict(request):
    ctx = {"test":"hola"}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx