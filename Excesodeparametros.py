def crear_usuario(nombre, apellido, edad, correo, activo, rol):
    return {"nombre": nombre, "apellido": apellido, "edad": edad,
            "correo": correo, "activo": activo, "rol": rol}
#
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    apellido: str
    edad: int
    correo: str
    activo: bool
    rol: str

def crear_usuario(usuario: Usuario) -> dict:
    return usuario.__dict__
