from django.contrib import admin
from django.db.models import Sum
from .models import *

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}


# ==========================================
# INLINES PARA PRODUCTO_COLOR
# ==========================================
class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 3
    fields = ['imagen', 'orden']

class VariacionInline(admin.TabularInline):
    model = VariacionProducto
    extra = 1


@admin.register(ProductoColor)
class ProductoColorAdmin(admin.ModelAdmin):
    list_display = ['producto', 'color', 'get_stock_color']
    list_filter = ['producto__categoria', 'color']
    search_fields = ['producto__nombre', 'color']
    inlines = [VariacionInline, ImagenProductoInline]

    # Optimización para no saturar la base de datos al listar los colores
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('producto').prefetch_related('variaciones')

    # Calcula el stock específico de ESTE color sumando sus talles
    def get_stock_color(self, obj):
        return sum(v.stock for v in obj.variaciones.all())
    get_stock_color.short_description = 'Stock por Color'


# ==========================================
# ADMIN DEL PRODUCTO PADRE
# ==========================================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'get_stock_total']
    list_filter = ['categoria']
    search_fields = ['nombre']
    prepopulated_fields = {'slug': ('nombre',)}

    # Optimización: Traemos los colores y las variaciones de esos colores en cascada
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Usamos '__' para indicarle a Django que viaje a través de la relación
        return queryset.select_related('categoria').prefetch_related('colores__variaciones')

    # Calcula el stock TOTAL del producto sumando todos los talles de todos los colores
    def get_stock_total(self, obj):
        # Viaja por cada color asociado al producto y suma el stock de sus variaciones
        return sum(
            variacion.stock 
            for color in obj.colores.all() 
            for variacion in color.variaciones.all()
        )
    get_stock_total.short_description = 'Stock Total (Global)'