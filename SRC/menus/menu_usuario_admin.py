from src.usuarios.usuarios import usuarios, modificar_rol_usuario
from src.automatizaciones.automatizaciones import mostrar_automatizaciones_activas
from src.menus.menu_dispositivos import menu_dispositivos

def menu_administrador(email_admin):
    nombre_usuario = usuarios[email_admin]["nombre"]

    while True:
        print(f"\nMenú Admin - Bienvenido Administrador: {nombre_usuario}")
        print("1. Consultar automatizaciones activas")
        print("2. Gestión de dispositivos")
        print("3. Modificar rol de un usuario")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_automatizaciones_activas()
            
        elif opcion == "2":
            menu_dispositivos(email_admin)
            
        elif opcion == "3":
            email_objetivo = input("Ingrese el email del usuario a modificar: ").strip()
            nuevo_rol = input("Nuevo rol (usuario/administrador): ").strip().lower()
            if nuevo_rol not in ["usuario", "administrador"]:
                print("❌ Rol inválido.")
                continue
            modificar_rol_usuario(email_objetivo, nuevo_rol)
            
        elif opcion == "4":
            print("👋 Cerrando sesión...")
            break
        
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
