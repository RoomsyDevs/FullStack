# usuarios.py -->se definen las clases Usuario y Administrador

from auth import validar_login, validar_telefono, validar_email, validar_rol, validar_contrasena, validar_email_unico 
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    apellido: str
    email: str
    contrasena: str
    rol: str
    telefono: str

class Anfitrion(Usuario):
    def __init__(self, nombre, apellido, email, contrasena, telefono):
        super().__init__(nombre, apellido, email, contrasena, "anfitrion", telefono)


class admin(Usuario):
    def __init__(self, nombre, apellido, username, email, contrasena):
        super().__init__(nombre, apellido, email, contrasena, "admin", telefono="N/A")
        self.username = username

usuarios = [
    admin('Florencia', 'Lorenzati', 'Florencier', 'florencia@gmail.com', 'flor123'),
    admin('Ignacio', 'Bentivoglio', 'Nacher','ignacio@gmail.com', 'nacho123'),
    Usuario('Gloria', 'López', 'gloria@gmail.com', 'gloria123', "anfitrion", "+5412345690"),
    Usuario('Marcos', 'Fernández', 'marcos@gmail.com', 'marcos123', "anfitrion", "+5412347890"),
    Usuario('Lucas', 'Martínez', 'lucas@gmail.com', 'lucas123', "+5412567890", "turista"),
    Usuario('Teodoro', 'Ramírez', 'teodoro@gmail.com', 'teo123', "+5434567890", "turista")
    ]

def iniciar_sesion():
    email = validar_email()
    contrasena = input("Contraseña:")

    for usuario in usuarios:
        if usuario.email == email:
            if validar_login(usuario, contrasena):
                print(f"\nBienvenido, {usuario.nombre} ({usuario.rol})")
                return usuario

    print("\nError: Mail o contraseña incorrectas.")
    return None

def registrar_usuario(usuarios):
    print("\n<<< Registro de usuario >>>")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = validar_email_unico(usuarios)
    contrasena = validar_contrasena()
    telefono = input("Ingrese su Teléfono (sin +54): ").strip()
    while not validar_telefono(telefono):
        print("Error, el número de telefono ingresado debe tener entre 10 y 11 dígitos, solo digitar números.")
        telefono = input ("Ingrese su Teléfono (sin +54): ").strip()
    telefono = "+54" + telefono
        

    rol = validar_rol()
    if rol == "anfitrion":
        nuevo_usuario = Anfitrion(nombre, apellido, email, contrasena, telefono)
    else:
        nuevo_usuario = Usuario(nombre, apellido, email, contrasena, telefono, "turista")

    usuarios.append(nuevo_usuario)
    print(f"\nUsuario registrado: {nuevo_usuario.nombre} {nuevo_usuario.apellido} {nuevo_usuario.telefono} ({nuevo_usuario.rol})")
    return nuevo_usuario

def modificar_usuario(admin):
    if admin.rol != "admin":
        print("\nError: Solo los administradores pueden modificar usuarios.")
        return
    
    print("\nUsuarios:")
    mostrar_usuarios()

    id_usuario = int(input("Elegi el número del usuario a editar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol != "admin":
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_apellido = input("Nuevo apellido: ")
        email_actual = usuarios[id_usuario].email
        nuevo_email = validar_email_unico(usuarios, email_actual)
        nuevo_telefono = input("Ingrese su nuevo telefono (sin +54): ").strip()
        while not validar_telefono(nuevo_telefono):
            print("Número inválido")
            nuevo_telefono = input("Ingrese su nuevo telefono (sin el +54: )")
        nuevo_telefono = "+54" + nuevo_telefono

        nueva_contrasena = validar_contrasena()

        for indice_usuario, usuario in enumerate(usuarios):
            if any(i != id_usuario and u.email == nuevo_email for i, u in enumerate(usuarios)):
                print("\nError: Este email ya se encuentra registrado.")
                return

        usuarios[id_usuario].nombre = nuevo_nombre
        usuarios[id_usuario].apellido = nuevo_apellido
        usuarios[id_usuario].email = nuevo_email
        usuarios[id_usuario].contrasena = nueva_contrasena
        usuarios[id_usuario].telefono = nuevo_telefono

        print("\nUsuario modificado con éxito")
    else:
        print("\nError: No se puede modificar a un usuario Administrador o el número es inválido")

def eliminar_usuario(admin):
    if admin.rol != "admin":
        print("\nError: Solo un administrador puede eliminar usuarios.")
        return

    print("\nUsuarios:")
    for indice_usuario, usuario in enumerate(usuarios, 1):
        print(f"{indice_usuario}. {usuario.nombre} {usuario.apellido} - {usuario.email} ({usuario.rol})")

    id_usuario = int(input("\nElegí el número del usuario que quiere eliminar: ")) - 1

    if 0 <= id_usuario < len(usuarios) and usuarios[id_usuario].rol != "admin":
        usuarios.pop(id_usuario)
        print("\nUsuario eliminado con éxito.")
    else:
        print("\nError: no se puede eliminar a un admin")

def mostrar_usuarios():
    print("\nLista de Usuarios: ")
    for indice_usuario, usuario in enumerate(usuarios, 1):
        print(f"{indice_usuario}. {usuario.nombre} {usuario.apellido} - {usuario.email} ({usuario.rol})")