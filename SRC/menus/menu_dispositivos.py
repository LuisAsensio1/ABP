from src.dispositivos.dispositivos import agregar_dispositivo, mostrar_todos_dispositivos, modificar_dispositivo, eliminar_dispositivo

def menu_dispositivos(email_admin):
    while True:
        print(f"\nMenú de Gestión de Dispositivos - Administrador: {email_admin}")
        print("1. Registrar dispositivo")
        print("2. Mostrar dispositivos")
        print("3. Modificar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver al menú anterior")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            email_usuario = input("Ingrese el email del usuario al que agregar el dispositivo: ").strip()
            nombre = input("Nombre del dispositivo: ").strip()
            print("1. Cámara de seguridad\n2. Sensor de movimiento")
            tipo_op = input("Opción: ").strip()
            if tipo_op == "1":
                tipo_disp = "cámara de seguridad"
            elif tipo_op == "2":
                tipo_disp = "sensor de movimiento"
            else:
                print("❌ Tipo inválido.")
                continue

            modelo = input("Modelo del dispositivo: ").strip()
            agregar_dispositivo(email_usuario, nombre, tipo_disp, modelo)

        elif opcion == "2":
            mostrar_todos_dispositivos()

        elif opcion == "3":
            email_usuario = input("Ingrese el email del usuario: ").strip()
            nombre = input("Ingrese el nombre del dispositivo a modificar: ").strip()
            nuevo_modelo = input("Ingrese el nuevo modelo (dejar vacío si no cambia): ").strip()
            estado_input = input("Ingrese el nuevo estado (encendido/apagado, dejar vacío si no cambia): ").strip().lower()
            
            nuevo_estado = None
            
            if estado_input == "encendido":
                nuevo_estado = True
            elif estado_input == "apagado":
                nuevo_estado = False
                
            modificar_dispositivo(email_usuario, nombre, nuevo_modelo or None, nuevo_estado)

        elif opcion == "4":
            email_usuario = input("Ingrese el email del usuario: ").strip()
            nombre_disp = input("Nombre del dispositivo a eliminar: ").strip()
            eliminar_dispositivo(email_usuario, nombre_disp)

        elif opcion == "5":
            print("👋 Volviendo al menú anterior...")
            return

        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
