from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nombre
    

class ProductoColor(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='colores')
    color = models.CharField(max_length=50)
    imagen_principal = models.ImageField(upload_to='productos/galeria/%Y/%m/%d')

    class Meta:
        verbose_name = "Color de Producto"
        verbose_name_plural = "Colores de Productos"  # <- Corregido aquí

    def __str__(self):
        return f"{self.producto.nombre} - {self.color}"
    

class ImagenProducto(models.Model):
    producto_color = models.ForeignKey(ProductoColor, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen = models.ImageField(upload_to='productos/galeria/%Y/%m/%d')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Imagen adicional"
        verbose_name_plural = "Imágenes adicionales"  # <- Corregido aquí
        ordering = ['orden']

    def __str__(self):
        return f"Imagen de {self.producto_color}"
    

class VariacionProducto(models.Model):
    producto_color = models.ForeignKey(ProductoColor, on_delete=models.CASCADE, related_name='variaciones')
    talle = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Variación de Producto"
        verbose_name_plural = "Variaciones de Productos"

    def __str__(self):
        # Corregido: accedemos de manera segura a través de producto_color
        return f'{self.producto_color.producto.nombre} - {self.producto_color.color} - Talle: {self.talle}'