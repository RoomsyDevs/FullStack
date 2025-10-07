from usuarios import registrar_usuario, iniciar_sesion, modificar_usuario, eliminar_usuario, mostrar_usuarios, modificar_cuenta, eliminar_cuenta
from hospedajes import registrar_hospedaje, mostrar_hospedaje_registrado, eliminar_hospedaje, mostrar_hospedaje, disponibilidad_hospedaje
from auth import validar_email_unico, validar_contrasena, validar_rol, validar_username_unico, validar_telefono
from conexion import conectar

def menu_anfitrion(usuario):
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
            registrar_hospedaje(usuario)
        elif opcion == '2':
            mostrar_hospedaje_registrado(usuario)
        elif opcion == '3':
            disponibilidad_hospedaje(usuario)
        elif opcion == '4':
            eliminar_hospedaje(usuario)
        elif opcion == '5':
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nuevo_apellido = input("Nuevo apellido: ").strip()
            nuevo_telefono = validar_telefono()
            nueva_contrasena = validar_contrasena()

            modificar_cuenta(usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena)

        elif opcion == '6':
            if eliminar_cuenta(usuario):
                break
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
            mostrar_hospedaje()
        elif opcion == '2':
            nuevo_nombre = input("Nuevo nombre: ").strip()
            nuevo_apellido = input("Nuevo apellido: ").strip()
            nuevo_telefono = validar_telefono()
            nueva_contrasena = validar_contrasena()

            modificar_cuenta(usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena)

        elif opcion == '3':
            if eliminar_cuenta(usuario):
                break
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
        print("3. Eliminar hospedaje")
        print("4. Ver usuarios")
        print("5. Ver hospedajes")
        print("6. Modificar usuario (No puede ser admin)")
        print("7. Cerrar sesión")

        opcion = input("Seleccionar una opción: ").strip()

        if opcion == '1':
            print("\n<<< Crear cuenta admin >>>")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = validar_email_unico()
            contrasena = validar_contrasena()
            username = validar_username_unico()
            registrar_usuario(nombre, apellido, email, contrasena, "N/A", "admin", username)
            print("Cuenta administrador creada con éxito!!")
        
        elif opcion == '2':
            id_usuario = int(input("Elija el número de id del usuario a eliminar: "))
            eliminar_usuario(id_usuario)
        elif opcion == '3':
            eliminar_hospedaje(usuario)
        elif opcion == '4':
            mostrar_usuarios()
        elif opcion == '5':
            mostrar_hospedaje()
        elif opcion == '6':
            id_usuario = int(input("Elija el número de id del usuario a modificar: ").strip())
            
            conn = conectar()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
            usuario_modificable = cursor.fetchone()

            if usuario_modificable and usuario_modificable["rol"] != "admin":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                nuevo_apellido = input("Nuevo apellido: ").strip()
                nuevo_telefono = validar_telefono()
                nueva_contrasena = validar_contrasena()

                modificar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena)
                print("Usuario modificado con éxito.")
            else:
                print("No se puede modificar a un usuario administrador.")

            conn.close()

        elif opcion == '7':
            print("Su sesión finalizó con éxito.")
            break
        else:
            print("Error, por favor ingrese una opción válida.")

def main():
    print("<<< Bienvenidos a RoomsyDevs >>>")

    while True:
        print("\nElegir una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver hospedajes publicados")
        print("4. Salir del programa")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            print("\n<<< Registro de nuevo usuario >>>")
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = validar_email_unico()
            contrasena = validar_contrasena()
            telefono = input("Teléfono (Sin el +54): ").strip()
            rol = validar_rol()

            if rol == "admin":
                username = validar_username_unico()
                registrar_usuario(nombre, apellido, email, contrasena, telefono, rol, username)
            else:
                registrar_usuario(nombre, apellido, email, contrasena, telefono, rol)

            print("Usuario registrado con éxito.")

        elif opcion == '2':
            print("\n<<< Iniciar sesión >>>")
            email = input("Email: ").strip()
            contrasena = input("Contraseña: ").strip()
            usuario = iniciar_sesion(email, contrasena)

            if usuario:
                if usuario.rol == "anfitrion":
                    menu_anfitrion(usuario)
                elif usuario.rol == "turista":
                    menu_turista(usuario)
                elif usuario.rol == "admin":
                    menu_admin(usuario)
                else:
                    print("Rol desconocido.")
            else:
                print("No se pudo iniciar sesión.")

        elif opcion == '3':
            mostrar_hospedaje()

        elif opcion == '4':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    print("Programa finalizado. ¡Gracias por usar RoomsyDevs!")

if __name__ == "__main__":
    main()