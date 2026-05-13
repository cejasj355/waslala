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
    imagen = models.ImageField(upload_to='productos/%Y/%m/%d', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen = models.ImageField(upload_to='productos/galeria/%Y/%m/%d')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Imagen adicional"
        verbose_name = "Imágenes adicionales"
        ordering = ['orden']

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
    
class VariacionProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variaciones')
    talle = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.producto.nombre} - {self.talle} - {self.color}'