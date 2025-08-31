# Calcular área de rectángulo en varios lugares
largo1, ancho1 = 10, 5
area1 = largo1 * ancho1

largo2, ancho2 = 8, 4
area2 = largo2 * ancho2
#
def calcular_area_rectangulo(largo: float, ancho: float) -> float:
    """Devuelve el área de un rectángulo."""
    return largo * ancho

area1 = calcular_area_rectangulo(10, 5)
area2 = calcular_area_rectangulo(8, 4)
