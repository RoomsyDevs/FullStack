# main.py --> menú e interaccion con usuario

from usuarios import registrar_usuario, iniciar_sesion, modificar_usuario, eliminar_usuario, usuarios
from hospedajes import registrar_hospedaje, mostrar_hospedaje_registrado, eliminar_hospedaje, mostrar_hospedajes

def registrar_usuarios():
    print("\n<<< Registrar nuevo usuario >>>")
    nuevo_usuario = registrar_usuario(usuarios) 

def main():
    print("<<< Bienvenidos a RoomsyDevs >>>")

    while True:
        print("\nElegir una opción:")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Ver los hospedajes registrados")
        print("4. Salir del programa")

        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == '1':
            registrar_usuario(usuarios)

        elif opcion == '2':
            usuario = iniciar_sesion()
            if usuario:
                if usuario.rol == "anfitrion":
                    while True:
                        print("\n<<<  Menú Anfitrión  >>>")
                        print("1. Registrar hospedaje")
                        print("2. Ver hospedajes publicados")
                        print("3. Eliminar hospedaje")
                        print("4. Editar usuario")
                        print("5. Eliminar cuenta")
                        print("6. Cerrar sesión")

                        opciones_de_anfitrion = input("Seleccionar una opción: ").strip()

                        if opciones_de_anfitrion == '1':
                            registrar_hospedaje(usuario)
                        elif opciones_de_anfitrion == '2':
                            mostrar_hospedaje_registrado(usuario)
                        elif opciones_de_anfitrion == '3':
                            eliminar_hospedaje(usuario)
                        elif opciones_de_anfitrion == '4':
                            modificar_usuario(usuario)
                        elif opciones_de_anfitrion == '5':
                            eliminar_usuario(usuario)
                        elif opciones_de_anfitrion == '6':
                            print("Su sesión finalizó con éxito.")
                            break
                        else:
                            print("Opción inválida, intente nuevamente.")

                else:
                    while True:
                        print("\n<<<  Menú Turista  >>>")
                        print(f"\nSesión iniciada como: {usuario.nombre} ({usuario.rol})")
                        print("Opciones disponibles:")
                        print("1. Ver hospedajes")
                        print("2. Editar usuario")
                        print("3. Eliminar cuenta")
                        print("4. Cerrar sesión")

                        opcion_estandar = input("Elegir una opción: ").strip()

                        if opcion_estandar == '1':
                            mostrar_hospedajes(usuario)
                        elif opcion_estandar == '2':
                            modificar_usuario(usuario)
                        elif opcion_estandar == '3':
                            eliminar_usuario(usuario)
                        elif opcion_estandar == '4':
                            print("Su sesión finalizó con éxito.")
                            break
                        else:
                            print("La opción es inválida, intente de nuevo")

            else:
                print("No se pudo iniciar sesión, vuelva a intentar!")
        
        elif opcion == '3':
            mostrar_hospedajes()

        elif opcion == '4':
            print("Usted esta saliendo del programa")
            break

        else:
            print("Error, por favor selecciona entre las opciones: 1, 2, 3, 4, 5 o 6")

    print("Cerrando programa. Vuelva pronto!")

if __name__ == "__main__":
    main()