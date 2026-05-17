def monto_total_carrito(request):
    total = 0
    if request.user.is_authenticated or True:
        for key, value in request.session.get("carrito", {}).items():
            total += int(value["cantidad"])
    return {"contador_carrito": total}