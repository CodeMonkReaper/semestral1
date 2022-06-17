from django.contrib import admin
from core.models import categoria, producto
# Register your models here.
class productoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion', 'categoria']
    search_fields = ['nombre','descripcion']
    list_filter = ['categoria']
admin.site.register(categoria,categoriaAdmin)
admin.site.register(producto,productoAdmin)

