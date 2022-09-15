from django.contrib import admin
from .models import Category, Post

# Para agregar titulo al list_filter
def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("title", "author", "published", "post_categories") # Lo que se mostrara en la seleccion en el panel admin, el ultimo es un campo especial que configuro con el def post_categories
    ordering = ("author", "published") # Los campos primario y secundario de ordenamiento
    search_fields = ("title","content","author__username", "categories__name") # Los campos en los que buscará con el boton de bsucar
    date_hierarchy= "published" # Forma de navegar entre fechas en el panel admin
    list_filter = ("author__username", ('categories__name', custom_titled_filter('Categoria'))) # Muestra la lista de filtros a la derecha, el segundo campo es uno eprsonalizado donde cmabio el titulo que muestra el filtro


    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)