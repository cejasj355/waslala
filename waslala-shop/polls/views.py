from django.shortcuts import render, get_object_or_404
from .models import Producto
# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html')

def catalogo(request):
    productos = Producto.objects.all()

    return render(request, 'polls/catalogo.html', {'productos': productos})

def producto(request, slug):
    #Obtengo los datos del producto seleccionado, por el slug
    producto = get_object_or_404(Producto, slug=slug)

    variaciones = producto.variaciones.all()

    return render(request, 'polls/producto.html', {
        'producto':producto,
        'variaciones': variaciones
    })

def login(request):
    return render(request, 'polls/login.html')

def carrito(request):
    return render(request, 'polls/carrito.html')

def checkout(request):
    return render(request, 'polls/checkout.html')

