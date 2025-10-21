from src.menus.menu_dispositivos import menu_dispositivos
from src.usuarios.usuarios import usuarios
from src.menus.menu_usuario_admin import menu_administrador
from src.menus.menu_usuario_estandar import menu_usuario


def menu_principal(email_usuario): 
    datos_usuario = usuarios[email_usuario]
    rol = datos_usuario["rol"]

    if rol == "administrador":
        menu_administrador(email_usuario)
    else:
        menu_usuario(email_usuario)
