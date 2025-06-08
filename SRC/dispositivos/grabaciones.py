import json
import os
from datetime import datetime
import threading
import time

# Ruta para guardar registros de grabaciones
RUTA_GRABACIONES = os.path.join("data", "grabaciones.json")

def cargar_grabaciones():
    """Carga el historial de grabaciones desde archivo JSON"""
    if os.path.exists(RUTA_GRABACIONES):
        with open(RUTA_GRABACIONES, "r") as f:
            return json.load(f)
    return {}

def guardar_grabaciones(grabaciones):
    """Guarda el historial de grabaciones en archivo JSON"""
    try:
        os.makedirs(os.path.dirname(RUTA_GRABACIONES), exist_ok=True)
        with open(RUTA_GRABACIONES, "w") as f:
            json.dump(grabaciones, f, indent=4)
    except Exception as e:
        print(f"❌ Error al guardar grabaciones: {e}")

def grabar(email, dispositivo, duracion_segundos=30, motivo="manual"):
    """
    Función principal para grabar con una cámara de seguridad
    
    Args:
        email (str): Email del usuario propietario del dispositivo
        dispositivo (str): Nombre del dispositivo a usar para grabar
        duracion_segundos (int): Duración de la grabación en segundos (default: 30)
        motivo (str): Motivo de la grabación ("manual", "movimiento", "programada")
    
    Returns:
        dict: Información sobre la grabación realizada
    """
    
    # Importar funciones necesarias
    from SRC.dispositivos.dispositivos import cargar_dispositivos, dispositivos
    from SRC.automatizaciones.automatizaciones import cargar_automatizaciones, automatizaciones
    
    # Verificar que el dispositivo existe y está disponible
    cargar_dispositivos()
    
    if email not in dispositivos or dispositivo not in dispositivos[email]:
        print(f"❌ Dispositivo '{dispositivo}' no encontrado para el usuario {email}")
        return {"exito": False, "error": "Dispositivo no encontrado"}
    
    # Verificar estado del dispositivo
    info_dispositivo = dispositivos[email][dispositivo]
    if info_dispositivo["estado"] != "encendido":
        print(f"❌ El dispositivo '{dispositivo}' está apagado")
        return {"exito": False, "error": "Dispositivo apagado"}
    
    # Verificar configuración de automatización
    cargar_automatizaciones()
    
    config_auto = None
    if email in automatizaciones and dispositivo in automatizaciones[email]:
        config_auto = automatizaciones[email][dispositivo]
        
        # Verificar si la automatización permite grabación
        if not config_auto.get("encendido", True):
            print(f"❌ La automatización del dispositivo '{dispositivo}' está desactivada")
            return {"exito": False, "error": "Automatización desactivada"}
    
    # Información de la grabación
    timestamp = datetime.now()
    archivo_grabacion = f"{email}_{dispositivo}_{timestamp.strftime('%Y%m%d_%H%M%S')}.mp4"
    
    # Simular inicio de grabación
    print(f"🎥 Iniciando grabación en '{dispositivo}'...")
    print(f"📹 Duración: {duracion_segundos} segundos")
    print(f"📁 Archivo: {archivo_grabacion}")
    print(f"⏰ Inicio: {timestamp.strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Simular proceso de grabación
    def proceso_grabacion():
        for i in range(duracion_segundos):
            time.sleep(1)
            if (i + 1) % 5 == 0:  # Mostrar progreso cada 5 segundos
                print(f"⏳ Grabando... {i + 1}/{duracion_segundos}s")
    
    # Ejecutar grabación
    hilo_grabacion = threading.Thread(target=proceso_grabacion)
    hilo_grabacion.start()
    hilo_grabacion.join()
    
    # Finalizar grabación
    timestamp_fin = datetime.now()
    print(f"✅ Grabación completada: {archivo_grabacion}")
    print(f"⏰ Fin: {timestamp_fin.strftime('%d/%m/%Y %H:%M:%S')}")
    
    # Registrar la grabación en el historial
    grabaciones = cargar_grabaciones()
    
    if email not in grabaciones:
        grabaciones[email] = {}
    
    if dispositivo not in grabaciones[email]:
        grabaciones[email][dispositivo] = []
    
    registro_grabacion = {
        "archivo": archivo_grabacion,
        "inicio": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        "fin": timestamp_fin.strftime('%Y-%m-%d %H:%M:%S'),
        "duracion_segundos": duracion_segundos,
        "motivo": motivo,
        "modelo_dispositivo": info_dispositivo["modelo"],
        "configuracion": config_auto if config_auto else "Sin automatización"
    }
    
    grabaciones[email][dispositivo].append(registro_grabacion)
    guardar_grabaciones(grabaciones)
    
    # Enviar notificación si está configurada
    if config_auto and config_auto.get("notificaciones", False) and motivo == "movimiento":
        enviar_notificacion(email, dispositivo, archivo_grabacion)
    
    return {
        "exito": True,
        "archivo": archivo_grabacion,
        "duracion": duracion_segundos,
        "inicio": timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        "fin": timestamp_fin.strftime('%Y-%m-%d %H:%M:%S')
    }

def grabar_por_movimiento(email, dispositivo):
    """Función específica para grabación activada por detección de movimiento"""
    print(f"🚨 Movimiento detectado en '{dispositivo}'")
    return grabar(email, dispositivo, duracion_segundos=60, motivo="movimiento")

def grabar_programada(email, dispositivo, duracion=120):
    """Función para grabación programada por horario"""
    print(f"⏰ Grabación programada iniciada en '{dispositivo}'")
    return grabar(email, dispositivo, duracion_segundos=duracion, motivo="programada")

def grabar_manual(email, dispositivo):
    """Función para grabación manual solicitada por el usuario"""
    print(f"👤 Grabación manual solicitada para '{dispositivo}'")
    
    # Pedir duración al usuario
    try:
        duracion = int(input("Duración en segundos (por defecto 30): ") or "30")
        if duracion <= 0:
            duracion = 30
    except ValueError:
        duracion = 30
    
    return grabar(email, dispositivo, duracion_segundos=duracion, motivo="manual")

def enviar_notificacion(email, dispositivo, archivo):
    """Simula el envío de una notificación al usuario"""
    print(f"📧 Notificación enviada a {email}:")
    print(f"   Dispositivo: {dispositivo}")
    print(f"   Grabación: {archivo}")
    print(f"   Motivo: Detección de movimiento")

def ver_historial_grabaciones(email, dispositivo=None):
    """Muestra el historial de grabaciones de un usuario"""
    grabaciones = cargar_grabaciones()
    
    if email not in grabaciones:
        print("⚠️ No hay grabaciones registradas para este usuario.")
        return
    
    print(f"\n📹 HISTORIAL DE GRABACIONES - {email}")
    print("=" * 50)
    
    dispositivos_usuario = grabaciones[email]
    
    if dispositivo:
        # Mostrar solo un dispositivo específico
        if dispositivo in dispositivos_usuario:
            mostrar_grabaciones_dispositivo(dispositivo, dispositivos_usuario[dispositivo])
        else:
            print(f"⚠️ No hay grabaciones para el dispositivo '{dispositivo}'")
    else:
        # Mostrar todos los dispositivos
        for nombre_disp, lista_grabaciones in dispositivos_usuario.items():
            mostrar_grabaciones_dispositivo(nombre_disp, lista_grabaciones)

def mostrar_grabaciones_dispositivo(nombre_dispositivo, grabaciones):
    """Función auxiliar para mostrar grabaciones de un dispositivo específico"""
    print(f"\n📷 {nombre_dispositivo}")
    print("-" * 30)
    
    if not grabaciones:
        print("  Sin grabaciones")
        return
    
    # Mostrar las últimas 5 grabaciones
    grabaciones_recientes = grabaciones[-5:]
    
    for grab in grabaciones_recientes:
        print(f"  📁 {grab['archivo']}")
        print(f"     ⏰ {grab['inicio']} - {grab['fin']}")
        print(f"     ⏱️  Duración: {grab['duracion_segundos']}s")
        print(f"     🔍 Motivo: {grab['motivo']}")
        print()
    
    if len(grabaciones) > 5:
        print(f"  ... y {len(grabaciones) - 5} grabaciones más")

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de grabación manual
    resultado = grabar("usuario@email.com", "camara_salon", 30, "manual")
    print(f"Resultado: {resultado}")
    
    # Ver historial
    ver_historial_grabaciones("usuario@email.com")