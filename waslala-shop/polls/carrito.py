class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session['carrito'] = {}
        self.carrito = carrito

        def add(self, producto):
            id = str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id] = {
                    "id": producto.id,
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                    "cantidad": 1,
                    "total": str(producto.precio)
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["total"] = str(float(self.carrito[id]["precio"] * self.carrito[id]["cantidad"]))
            self.save()
        def save(self):
            self.session["carrito"] = self.carrito
            self.session.modified = True
