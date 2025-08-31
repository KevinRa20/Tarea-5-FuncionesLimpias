precio1 = 100
iva1 = precio1 * 0.15
total1 = precio1 + iva1

precio2 = 250
iva2 = precio2 * 0.15
total2 = precio2 + iva2

def calcular_total(precio: float, iva: float = 0.15) -> float:
    """Calcula el total aplicando IVA."""
    return precio * (1 + iva)

total1 = calcular_total(100)
total2 = calcular_total(250)
