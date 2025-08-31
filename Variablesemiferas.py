def obtener_descuento(precio):
    descuento = precio * 0.1
    precio_final = precio - descuento
    return precio_final
#
def obtener_descuento(precio: float) -> float:
    return precio * 0.9
