usuarios = {}

def registrar_admin_unico(nombre, email, contrasena):
    if any(usuario["rol"] == "administrador" for usuario in usuarios.values()):
        return 
    
    if "@" not in email and "." not in email:
        print("❌ Email inválido. Debe tener formato nombre@dominio.com")
        return

    if len(contrasena) < 6:
        print("❌ La contraseña debe tener al menos 6 caracteres.")
        return
    
    if " " in contrasena:
        print("La contraseña no debe contener espacios en blanco.")
        return
    
    usuarios[email] = {
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": "administrador"
    }
    
    print(f"✅ Administrador '{nombre}' registrado correctamente.")
    
def registrar_usuario(nombre, email, contrasena, rol="usuario"):

    if "@" not in email and "." not in email:
        print("❌ Email inválido. Debe tener formato nombre@dominio.com")
        return

    if len(contrasena) < 6:
        print("❌ La contraseña debe tener al menos 6 caracteres.")
        return
    
    if " " in contrasena:
        print("La contraseña no debe contener espacios en blanco.")
        return

    # Verificar duplicado
    if email in usuarios:
        print("❌ Ya existe un usuario con ese email.")
        return
    
    # Verificar si ya existe un administrador
    if rol == "administrador" and any(u["rol"] == "administrador" for u in usuarios.values()):
        print("❌ Ya existe un administrador registrado.")
        return

    usuarios[email] = {
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": rol
    }
    
def login(email, contrasena):
    if email in usuarios and usuarios[email]["contrasena"] == contrasena:
        print(f"Bienvenido! - {usuarios[email]['nombre']}")
        return usuarios[email]
    else:
        print("❌ Error: El email o la contraseña ingresados son inválidos.")

def modificar_rol_usuario(email_objetivo, nuevo_rol):
    if email_objetivo not in usuarios:
        print("❌ Usuario no encontrado.")
        return
    usuarios[email_objetivo]["rol"] = nuevo_rol
    print(f"✅ Rol de {email_objetivo} cambiado a {nuevo_rol}.")
    
def mostrar_datos_personales(email_actual):
    usuario = usuarios.get(email_actual)
    if not usuario:
        print("❌ Usuario no encontrado.")
        return
    
    print(f"Mis datos personales: ")
    print(f"Email: {email_actual}")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Rol: {usuario['rol']}")