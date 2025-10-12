from conexion import conectar

class Auth:
    def __init__(self):
        self.__intentos = 0

    @staticmethod
    def validar_email():
        while True:
            email = input("Email: ").strip()
            if "@" in email and "." in email:
                return email
            else:
                print("Error: el email debe finalizar con un dominio válido.")

    @staticmethod
    def validar_email_unico(email_actual=None):
        while True:
            email = Auth.validar_email()
            if email == email_actual:
                return email
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE email = %s", (email,))
            existe = cursor.fetchone()[0]
            conn.close()
            if existe == 0:
                return email
            else:
                print("Este email ya está registrado. Intente nuevamente con otro.")

    @staticmethod
    def validar_contrasena():
        while True:
            contrasena = input("Contraseña (mínimo 6 caracteres): ")
            if len(contrasena) >= 6:
                return contrasena
            else:
                print("La contraseña debe tener al menos 6 caracteres.")

    @staticmethod
    def validar_telefono():
        while True:
            telefono = input("Nuevo teléfono (Sin el +54): ").strip()
            if telefono.isdigit() and 7 <= len(telefono) <= 15:
                return telefono
            print("El teléfono debe contener solo números y tener entre 9 a 10 dígitos.")

    @staticmethod
    def validar_rol():
        while True:
            rol = input("Roles (anfitrion / turista): ").strip().lower()
            if rol in ["anfitrion", "turista"]:
                return rol
            else:
                print("Error: El rol solo puede ser 'anfitrion' o 'turista'")

    @staticmethod
    def validar_username_unico():
        while True:
            username = input("Username: ").strip()
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM usuarios WHERE username = %s", (username,))
            existe = cursor.fetchone()[0]
            conn.close()
            if existe == 0:
                return username
            else:
                print("Este username ya está en uso. Intente nuevamente con otro.")


    @staticmethod
    def validar_precio():
        while True:
            try:
                precio = float(input("Precio por noche: ").strip())
                if precio > 0:
                    return precio
                else:
                    print("El precio no puede ser negativo, ni 0.")
            except ValueError:
                print("Debe ingresar un número válido.")
            
    @staticmethod
    def es_modificable(id_usuario):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT rol FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
        usuario = cursor.fetchone()
        conn.close()
        if not usuario:
            print("El usuario no existe o está inactivo.")
            return False
        if usuario["rol"] == "admin":
            print("No se puede modificar a otro administrador.")
            return False
        return True
