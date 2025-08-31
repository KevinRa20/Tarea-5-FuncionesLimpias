def procesar_datos(lista):
    resultados = []
    for dato in lista:
        if dato > 0:
            cuadrado = dato ** 2
            if cuadrado % 2 == 0:
                resultados.append((dato, cuadrado))
    return resultados
#
def es_positivo(num: int) -> bool:
    return num > 0

def calcular_cuadrado(num: int) -> int:
    return num ** 2

def es_par(num: int) -> bool:
    return num % 2 == 0

def procesar_datos(lista: list[int]) -> list[tuple[int, int]]:
    return [
        (dato, cuadrado)
        for dato in lista
        if es_positivo(dato) and es_par(cuadrado := calcular_cuadrado(dato))
    ]
