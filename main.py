from src.usuarios.usuarios import usuarios, login, registrar_usuario, registrar_admin_unico
from router import menu_principal

def menu_ingreso():
    print("Bienvenido al Sistema de Gestión")
    while True:
        if any(u["rol"] == "administrador" for u in usuarios.values()):
            break  # Ya hay admin, salir del bucle

        print("\n🔒 No hay administrador registrado. Debe crear uno primero.")
        nombre = input("Nombre del administrador: ").strip()
        email = input("Email: ").strip()
        contrasena = input("Contraseña: ").strip()
        
        registrar_admin_unico(nombre, email, contrasena)
        
        # Verificar si se registró correctamente
        if any(u["rol"] == "administrador" for u in usuarios.values()):
            print("✅ Administrador registrado correctamente.")
            break
        else:
            print("❌ Intente registrarlo nuevamente.\n")

    while True:
        print("\nMenú de Ingreso")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")
        
        opcion = input("Seleccione una opción:\n > ").strip()
        
        if opcion == "1":
            print("\nInicio de Sesión")
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()
            exito = login(email, contraseña)
            if exito:
                print(f"✅ Sesión iniciada correctamente. Bienvenido {usuarios[email]['nombre']}!")
                menu_principal(email)
            else:
                print("❌ Email o contraseña incorrectos.")

        elif opcion == "2":
            print("\nRegistro de usuario")
            nombre = input("Nombre: ").strip()
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()

            registrar_usuario(nombre, email, contraseña, rol="usuario")

        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida.")
            
if __name__ == "__main__":
    menu_ingreso()
            