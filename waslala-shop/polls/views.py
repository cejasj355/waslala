from django.shortcuts import render, get_object_or_404
from .models import *
from .carrito import Carrito
from django.http import JsonResponse
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html')

def catalogo(request):
    productos = Producto.objects.all()

    return render(request, 'polls/catalogo.html', {'productos': productos})

def producto(request, slug):
    # Obtengo los datos del producto seleccionado, por el slug
    producto = get_object_or_404(Producto, slug=slug)

    # CORRECCIÓN: Filtramos las variaciones pasando a través de ProductoColor
    variaciones = VariacionProducto.objects.filter(producto_color__producto=producto)

    return render(request, 'polls/producto.html', {
        'producto': producto,
        'variaciones': variaciones
    })

def login(request):
    return render(request, 'polls/login.html')

def carrito(request):
    return render(request, 'polls/carrito.html')

def checkout(request):
    return render(request, 'polls/checkout.html')

def agregar_ajax(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.add(producto=producto)
    return JsonResponse({
        'cart_count': len(carrito.carrito),
        'message': f'{producto.name} agregado correctamente'
    })

