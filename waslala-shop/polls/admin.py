from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 3
    fields = ['imagen', 'orden']

 
class VariacionInline(admin.TabularInline):
    model = VariacionProducto
    extra = 1


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'get_stock_total']
    list_filter = ['categoria'] # Agrega filtros laterales
    search_fields = ['nombre']   # Permite buscar por nombre
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [VariacionInline, ImagenProductoInline]

    # Esto hace que el admin traiga las variaciones de un solo golpe (JOIN)
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('variaciones', 'imagenes_adicionales')

    def get_stock_total(self, obj):
        return sum(v.stock for v in obj.variaciones.all())
    get_stock_total.short_description = 'Stock Total'