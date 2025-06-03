def menu_usuario(email_actual):
    nombre_usuario = usuarios.usuario[email_actual]["nombre"]

    while True:
        print(f"\n--- MENÚ USUARIO - Bienvenido {nombre_usuario} ---")
        print("1. Consultar mis datos personales")
        print("2. Ejecutar automatización")
        print("3. Consultar mis dispositivos")
        print("4. Modificar configuración de mis dispositivos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios.buscar_usuario(email_actual)
        elif opcion == "2":
            dispositivos.consultar_automatizaciones_activas()  # o ejecuta alguna simulación
        elif opcion == "3":
            dispositivos.listar_dispositivos_usuario(email_actual)
        elif opcion == "4":
            dispositivos.modificar_configuracion_dispositivo(email_actual)
        elif opcion == "5":
            print("👋 Cerrando sesión...")
            break
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
