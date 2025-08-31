def verificar_usuario(usuario):
    if usuario:
        if usuario["activo"]:
            if usuario["rol"] == "admin":
                return "Acceso concedido"
            else:
                return "Rol inválido"
        else:
            return "Usuario inactivo"
    else:
        return "Usuario no existe"
def verificar_usuario(usuario: dict) -> str:
    if not usuario:
        return "Usuario no existe"
    if not usuario["activo"]:
        return "Usuario inactivo"
    if usuario["rol"] != "admin":
        return "Rol inválido"
    return "Acceso concedido"
