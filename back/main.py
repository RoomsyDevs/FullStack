from usuarios import admin, usuario
from hospedajes import hospedaje
from validaciones import Auth
from conexion import conectar


def menu_anfitrion(usuario):
    auth = Auth()
    while True:
        print("\n<<< Menú Anfitrión >>>")
        print("1. Registrar hospedaje")
        print("2. Ver hospedajes publicados")
        print("3. Cambiar disponibilidad de hospedaje")
        print("4. Eliminar hospedaje")
        print("5. Editar usuario")
        print("6. Eliminar cuenta")
        print("7. Cerrar sesión")

        opcion = input("Seleccionar una opción: ").strip()

        if opcion == '1':
            titulo = input("Titulo: ").strip()
            precio_por_noche = auth.validar_precio()
            descripcion = input("Descripción: ").strip()
            ciudad = input("Ciudad del hospedaje: ").strip()
            provincia = input("Provincia: ").strip()
            capacidad = int(input("Capacidad máxima del hospedaje: ").strip())


            hospedaje.registrar_hospedaje(
            anfitrion_id = usuario.id,
            titulo = titulo,
            precio_por_noche = precio_por_noche,
            descripcion = descripcion,
            ciudad = ciudad,
            provincia = provincia,
            capacidad = capacidad
            )
        elif opcion == '2':
            hospedaje.mostrar_hospedaje_registrado(usuario)
        elif opcion == '3':
            hospedaje.disponibilidad_hospedaje(usuario)
        elif opcion == '4':
            hospedaje.eliminar_hospedaje(usuario)
        elif opcion == '5':
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nuevo_apellido = input("Nuevo apellido: ").strip()
            nuevo_telefono = Auth.validar_telefono()
            nueva_contrasena = Auth.validar_contrasena()

            usuario.modificar_cuenta(nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena)
            print("\nUsuario modificado con éxito.")

        elif opcion == '6':
                confirmacion = input("¿Estás seguro de que querés eliminar tu cuenta? Esta acción es irreversible (s/n): ").strip().lower()
                if confirmacion == 's':
                    if usuario.eliminar_cuenta():
                        print("Cerrando sesión...")
                    break
                elif confirmacion == 'n':
                    print("Operación cancelada.")
                else:
                    print("Opción inválida. Por favor ingresá 's' o 'n'.")
        elif opcion == '7':
            print("Su sesión finalizó con éxito.")
            break
        else:
            print("Opción inválida, intente nuevamente.")


def menu_turista(usuario):
    while True:
        print("\n<<< Menú Turista >>>")
        print("1. Ver hospedajes")
        print("2. Editar usuario")
        print("3. Eliminar cuenta")
        print("4. Cerrar sesión")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            hospedaje.mostrar_hospedaje()
        elif opcion == '2':
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nuevo_apellido = input("Nuevo apellido: ").strip()
            nuevo_telefono = Auth.validar_telefono()
            nueva_contrasena = Auth.validar_contrasena()
            usuario.modificar_cuenta(nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena)

        elif opcion == '3':
                confirmacion = input("¿Estás seguro de que querés eliminar tu cuenta? Esta acción es irreversible (s/n): ").strip().lower()
                if confirmacion == 's':
                    if usuario.eliminar_cuenta():
                        print("Cerrando sesión...")
                    break
                elif confirmacion == 'n':
                    print("Operación cancelada.")
                else:
                    print("Opción inválida. Por favor ingresá 's' o 'n'.")
        elif opcion == '4':
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida, intente nuevamente")

def menu_admin(usuario):
    while True:
        print("\n<<< Menú Administrador >>>")
        print("1. Crear cuenta admin")
        print("2. Eliminar usuario")
        print("3. Ver usuarios")
        print("4. Ver hospedajes")
        print("5. Modificar usuario (No puede ser admin)")
        print("6. Cerrar sesión")

        opcion = input("Seleccionar una opción: ").strip()

        if opcion == '1':
            print("\n<<< Crear cuenta admin >>>")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = Auth().validar_email_unico()
            contrasena = Auth.validar_contrasena()
            username = Auth().validar_username_unico()
            usuario.crear_admin(nombre, apellido, email, contrasena, "admin", username)
            print("Cuenta administrador creada con éxito!!")
        
        elif opcion == '2':
            admin.mostrar_usuarios()
            id_usuario = int(input("Elija el número de id del usuario a eliminar: "))
            confirmacion = input("¿Estás seguro de que querés eliminar tu cuenta? Esta acción es irreversible (s/n): ").strip().lower()
            if confirmacion == 's':
                if admin.eliminar_usuario(id_usuario):
                    print("Usuario eliminado con éxito.")
            elif confirmacion == 'n':
                print("Operación cancelada.")
        elif opcion == '3':
            admin.mostrar_usuarios()
        elif opcion == '4':
            hospedaje.mostrar_hospedaje()
        elif opcion == '5':
            admin.mostrar_usuarios()
            id_usuario = int(input("Elija el número de id del usuario a modificar: "))

            if not Auth.es_modificable(id_usuario):
                continue
            else:
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nuevo_apellido = input("Nuevo apellido: ").strip()
                nuevo_telefono = Auth.validar_telefono()
                nueva_contrasena = Auth.validar_contrasena()
                nuevo_rol = Auth.validar_rol()

                admin.modificar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena, nuevo_rol)
        
        elif opcion == '6':
            print ("Cerrando sesión...")
            break


def main():
    print("<<< Bienvenidos a RoomsyDevs >>>")
    auth = Auth()

    while True:
        print("\nElegir una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver hospedajes publicados")
        print("4. Salir del programa")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            registrar_usuario_input(auth)

        elif opcion == '2':
            print("\n<<< Iniciar sesión >>>")
            email = input("Email: ").strip()
            contrasena = Auth.validar_contrasena()
            usuario_login = usuario.iniciar_sesion(email, contrasena)

            if not usuario_login:
                print("Usuario o contraseña incorrectos.")
            elif usuario:
                if usuario_login.rol == "anfitrion":
                    menu_anfitrion(usuario_login)
                elif usuario_login.rol == "turista":
                    menu_turista(usuario_login)
                elif usuario_login.rol == "admin":
                    menu_admin(usuario_login)
                else:
                    print("Rol desconocido.")
            else:
                print("No se pudo iniciar sesión.")

        elif opcion == '3':
            hospedaje.mostrar_hospedaje()

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    print("Programa finalizado. ¡Gracias por usar RoomsyDevs!")

def registrar_usuario_input(auth):
    print("\n<<< Registro de nuevo usuario >>>")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = Auth.validar_email_unico()
    contrasena = Auth.validar_contrasena()
    telefono = Auth.validar_telefono()
    rol = Auth.validar_rol()
    if rol == "admin":
        username = Auth.validar_username_unico()
        admin.crear_admin(nombre, apellido, email, contrasena, telefono, rol, username)
    else:
        usuario.registrar_usuario(nombre, apellido, email, contrasena, telefono, rol)
    print("Usuario registrado con éxito.") 

if __name__ == "__main__":
    main()