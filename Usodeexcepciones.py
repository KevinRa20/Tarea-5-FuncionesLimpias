def obtener_numero(texto):
    try:
        return int(texto)
    except:
        return 0
#
def obtener_numero(texto: str) -> int:
    if texto.isdigit():
        return int(texto)
    return 0
