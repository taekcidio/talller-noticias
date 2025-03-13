from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'publicada')  # Campos visibles en la lista
    list_filter = ('publicada', 'fecha_publicacion')  # Filtros laterales
    search_fields = ('titulo', 'resumen', 'detalle')  # Barra de búsqueda
    ordering = ('-fecha_publicacion',)  # Orden descendente por fecha
