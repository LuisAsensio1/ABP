from datetime import datetime
from src.dispositivos.dispositivos import dispositivos

automatizaciones = {}

def pedir_hora(mensaje):
    while True:
        hora_str = input(mensaje)
        try:
            hora_obj = datetime.strptime(hora_str, "%H:%M")
            return hora_obj.strftime("%H:%M")
        except:
            print("Debe ingresar un horario valido. HH:MM")

def configurar_automatizacion(email_actual, dispositivo, nuevo_estado, hora_encendido, hora_apagado):
    if email_actual not in automatizaciones:
        automatizaciones[email_actual] = {}
    
    if dispositivo not in automatizaciones[email_actual]:
        automatizaciones[email_actual][dispositivo] = {}
    
    automatizaciones[email_actual][dispositivo]["programacion_horaria"] = {
        "estado": nuevo_estado,
        "hora_encendido": hora_encendido,
        "hora_apagado": hora_apagado
    }
    
    print(f"✅ La automatización para el '{dispositivo}' fue configurada correctamente.")

def ejecutar_automatizacion(email_actual):
    if email_actual not in automatizaciones:
        print("❌ Usuario no encontrado.")
        return
    # Conseguir la hora actual con datetime.now() y darle formato str con .strftime("%H:%M") 
    ahora = datetime.now().strftime("%H:%M")  

    for dispositivo, datos in automatizaciones[email_actual].items():
        programado = datos.get("programacion_horaria")
        if not programado or not programado.get("estado"):
            continue  # De no encontrar una automatización activa, saltamos con continue

        # Verificar si la hora actual está dentro del rango de encendido
        hora_encendido = programado["hora_encendido"]
        hora_apagado = programado["hora_apagado"]

        # Validación considerando cruce de medianoche
        if hora_encendido <= hora_apagado:  # misma jornada
            encendido = hora_encendido <= ahora <= hora_apagado
        else:  # cruza medianoche
            encendido = ahora >= hora_encendido or ahora <= hora_apagado

        datos["estado_disp"] = encendido
        if email_actual in dispositivos and dispositivo in dispositivos[email_actual]:
            dispositivos[email_actual][dispositivo]["estado_disp"] = encendido

        estado_texto = "encendido" if encendido else "apagado"
        print(f"✅ Su dispositivo: {dispositivo} se encuentra {estado_texto} automáticamente a las {ahora}.")

def mostrar_automatizaciones_activas():
    if not automatizaciones:
        print("⚠️ No hay automatizaciones configuradas.")
        return

    for email, dispositivos_usuario in automatizaciones.items():
        automatizaciones_dispositivos_activas = {
            nombre_disp: datos
            for nombre_disp, datos in dispositivos_usuario.items()
            if datos.get("programacion_horaria", {}).get("estado")
        } # -> Aqui consultamos los dispositivos que tengan automatizaciones activas

        if not automatizaciones_dispositivos_activas: 
            continue  # -> Aquí saltamos los que no las tienen activas

        print(f"\n📧 Usuario: {email}")
        for nombre_disp, datos in automatizaciones_dispositivos_activas.items(): # Utilizamos el bucle for para imprimir los resultados
            estado_actual = "encendido" if datos.get("estado") else "apagado"
            programado = datos["programacion_horaria"]
            print(f"Dispositivo: {nombre_disp} - Estado: {estado_actual}")
            print(f"Automatización activa:")
            print(f"Hora encendido: {programado['hora_encendido']}")
            print(f"Hora apagado : {programado['hora_apagado']}")
            