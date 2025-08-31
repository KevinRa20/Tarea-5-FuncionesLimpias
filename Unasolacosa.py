def procesar_pedido(pedido):
    # validar
    if not pedido["items"]:
        return "Pedido vacío"
    # calcular total
    total = sum(item["precio"] for item in pedido["items"])
    # imprimir resultado
    print(f"Total del pedido: {total}")
    return total
#
def validar_pedido(pedido: dict) -> bool:
    return bool(pedido.get("items"))

def calcular_total_pedido(pedido: dict) -> float:
    return sum(item["precio"] for item in pedido["items"])

def mostrar_total(total: float):
    print(f"Total del pedido: {total}")

if validar_pedido(pedido := {"items": [{"precio": 50}, {"precio": 30}]}):
    total = calcular_total_pedido(pedido)
    mostrar_total(total)
