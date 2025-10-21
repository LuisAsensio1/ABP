from src.usuarios.usuarios import usuarios

dispositivos = {}

def agregar_dispositivo(email, nombre, tipo_disp, modelo):
    if email not in usuarios:
        print(f"❌ No se puede agregar dispositivo. El usuario '{email}' no existe.")
        return
    
    if usuarios[email]["rol"] == "administrador":
        print("❌ No se pueden agregar dispositivos a un administrador.")
        return
    
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    
    if not modelo:
        print("❌ El modelo no puede estar vacío.")
        return

    if email not in dispositivos:
        dispositivos[email] = {}

    if nombre in dispositivos[email]:
        print("❌ Ya existe un dispositivo con ese nombre.")
        return

    dispositivos[email][nombre] = {
        "tipo": tipo_disp,
        "modelo": modelo,
        "estado_disp": False 
    }
    
    print(f"✅ Dispositivo '{nombre}' ({tipo_disp}) agregado correctamente.")

def mostrar_todos_dispositivos():
    if not dispositivos:
        print("⚠️ No hay dispositivos registrados.")
        return

    for email, disp_usuario in dispositivos.items():
        if disp_usuario: 
            print(f"\n📧 Usuario: {email}")
            for nombre, info in disp_usuario.items():
                estado_actual = "encendido" if info['estado_disp'] else "apagado"
                print(f"- {nombre} ({info['modelo']}) - Estado: {estado_actual}")

def mostrar_dispositivos_usuario(email_actual):
    if email_actual in dispositivos:
        print(f"\n📋 Dispositivos para {email_actual}:")
        for nombre, datos in dispositivos[email_actual].items():
            estado = "encendido" if datos['estado_disp'] else "apagado"
            print(f"- {nombre} ({datos['modelo']}) - Estado: {estado}")
    else:
        print("⚠️ No se encontraron dispositivos para este usuario.")

def eliminar_dispositivo(email, nombre):
    if email not in dispositivos or not dispositivos[email]:
        print("❌ El usuario no tiene dispositivos registrados.")
        return
    
    dispositivo = dispositivos[email].pop(nombre, None)
    
    if dispositivo:
        print(f"✅ Dispositivo '{nombre}' eliminado correctamente.")
    else:
        print("❌ Dispositivo no encontrado.")

def modificar_dispositivo(email, nombre, nuevo_modelo = None, nuevo_estado = None):
    if email not in dispositivos or not dispositivos[email]:
        print("❌ El usuario no tiene dispositivos registrados.")
        return
    
    if nombre not in dispositivos[email]:
        print("❌ Dispositivo no encontrado.")
        return
    
    if nuevo_modelo:
        dispositivos[email][nombre]["modelo"] = nuevo_modelo
    if nuevo_estado in ["encendido", "apagado"]:
        dispositivos[email][nombre]["estado_disp"] = nuevo_estado
        
    print(f"✅ Dispositivo '{nombre}' actualizado.")
    