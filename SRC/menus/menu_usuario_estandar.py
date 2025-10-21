from src.usuarios.usuarios import usuarios, mostrar_datos_personales
from src.dispositivos.dispositivos import dispositivos, mostrar_dispositivos_usuario
from src.automatizaciones.automatizaciones import automatizaciones, configurar_automatizacion, pedir_hora, ejecutar_automatizacion

def menu_usuario(email_actual):
    nombre_usuario = usuarios[email_actual]["nombre"]

    while True:
        print(f"\nMenú del Usuario - Bienvenido {nombre_usuario}")
        print("1. Consultar mis datos personales")
        print("2. Activar y Configurar Automatización")
        print("3. Ejecutar acción") 
        print("4. Consultar mis dispositivos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos_personales(email_actual)

        elif opcion == "2":
            # Verificar que el usuario tenga dispositivos
            if email_actual not in dispositivos or not dispositivos[email_actual]:
                print("❌ No tiene dispositivos registrados.")
            else:
                # Inicializar automatizaciones para cada dispositivo si no existe
                if email_actual not in automatizaciones:
                    automatizaciones[email_actual] = {}

                for nombre_disp in dispositivos[email_actual]:
                    if nombre_disp not in automatizaciones[email_actual]:
                        automatizaciones[email_actual][nombre_disp] = {}

                # Mostrar los dispositivos disponibles
                lista_dispositivos = list(dispositivos[email_actual].keys())

                print("\n📋 Dispositivos disponibles para automatización:")
                for i, nombre in enumerate(lista_dispositivos):
                    print(f"{i+1}. {nombre} - Estado actual: {dispositivos[email_actual][nombre]['estado_disp']}")

                try:
                    opcion_usuario = int(input("Seleccione un dispositivo por número: "))
                    if 1 <= opcion_usuario <= len(lista_dispositivos):
                        dispositivo_seleccionado = lista_dispositivos[opcion_usuario - 1]

                        # Preguntar si se activa la automatización
                        activar = input("¿Desea activar la automatización horaria? (s/n): ").strip().lower()
                        nuevo_estado = True if activar == "s" else False

                        # Pedir horarios de encendido y apagado
                        hora_encendido = pedir_hora("Ingrese el horario de encendido deseado (HH:MM): ")
                        hora_apagado = pedir_hora("Ingrese el horario de apagado deseado (HH:MM): ")

                        # Guardar la automatización
                        configurar_automatizacion(
                            email_actual, 
                            dispositivo_seleccionado, 
                            nuevo_estado, 
                            hora_encendido, 
                            hora_apagado
                        )
                    else:
                        print("❌ Opción fuera de rango.")
                except ValueError:
                    print("❌ Entrada inválida.")

        elif opcion == "3":
            print("\n🔄 Ejecutando acciones automáticas de tus dispositivos...")
            ejecutar_automatizacion(email_actual)

        elif opcion == "4":
            mostrar_dispositivos_usuario(email_actual)

        elif opcion == "5":
            print("👋 Cerrando sesión...")
            break

        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
