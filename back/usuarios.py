from conexion import conectar

class usuario:
    def __init__(self, id, nombre, apellido, email, contrasena, rol, telefono):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.rol = rol
        self.telefono = telefono

    # --- US10: Eliminar usuario (solo Admin) ---
    def eliminar_usuario(self, id_usuario):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s AND rol != 'admin'", (id_usuario,))
        conn.commit()
        conn.close()
        print("Usuario eliminado definitivamente.")

    # --- US11: Eliminar mi propia cuenta ---
    def eliminar_cuenta(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (self.id,))
        conn.commit()
        conn.close()
        print("Tu cuenta ha sido eliminada definitivamente.")
   
    @classmethod
    def registrar_usuario(cls, nombre, apellido, email, contrasena, telefono, rol, username=None):
        conn = conectar()
        cursor = conn.cursor()

        if rol == "admin":
            cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, rol, estado, username)
            VALUES (%s, %s, %s, %s, %s, %s, 1, %s)
            """, (nombre, apellido, email, contrasena, telefono, rol, username))
        else:
            cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, rol, estado)
            VALUES (%s, %s, %s, %s, %s, %s, 1)
            """, (nombre, apellido, email, contrasena, telefono, rol))


        conn.commit()
        conn.close()

    @classmethod
    def iniciar_sesion(cls, email, contrasena):
        conn= conectar()
        cursor =conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND estado = 1", (email,))
        usuario = cursor.fetchone()
        conn.close()

        if usuario and usuario["contrasena"] == contrasena:
            if usuario["rol"] == "admin":
                return admin(usuario["id"], usuario["nombre"], usuario["apellido"], usuario["email"], usuario["contrasena"], usuario["username"])
            elif usuario["rol"] == "anfitrion":
                return anfitrion(
                id=usuario["id"],
                nombre=usuario["nombre"],
                apellido=usuario["apellido"],
                email=usuario["email"],
                contrasena=usuario["contrasena"],
                rol=usuario["rol"],
                telefono=usuario["telefono"]
                )

            elif usuario["rol"] == "turista":
                return turista(
                    id=usuario["id"],
                    nombre=usuario["nombre"],
                    apellido=usuario["apellido"],
                    email=usuario["email"],
                    contrasena=usuario["contrasena"],
                    rol=usuario["rol"],
                    telefono=usuario["telefono"]
                )

            else:
                return None

    @staticmethod        
    def mostrar_usuarios():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE estado = 1")
        usuarios = cursor.fetchall()
        conn.close()

        for u in usuarios:
            print(f"{u['id']}. {u['nombre']} {u['apellido']} {u['email']} ({u['rol']})")
        

    def modificar_cuenta(self, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE usuarios
            SET nombre = %s, apellido = %s, telefono = %s, contrasena = %s
            WHERE id = %s
        """, (self.id, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena))
        conn.commit()
        conn.close()


class admin(usuario):
    def __init__(self, id, nombre, apellido, email, contrasena, username):
        super().__init__(id, nombre, apellido, email, contrasena, "admin", telefono="N/A")
        self.username = username

    @classmethod
    def crear_admin(cls, nombre, apellido, email, contrasena, rol, username):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, rol, estado, username)
            VALUES (%s, %s, %s, %s, %s, %s, 1, %s)
        """, (nombre, apellido, email, contrasena, "N/A", "admin", username))
        conn.commit()
        conn.close()
        print("Usuario administrador creado con éxito.")
        return True    

    @staticmethod
    def eliminar_usuario(id_usuario):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
        usuario = cursor.fetchone()

        if usuario and usuario["rol"] != "admin":
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            conn.commit()
            print(f"El usuario {usuario['nombre']} {usuario['apellido']} ha sido eliminado.")
        else:
            print("No se puede eliminar este usuario (puede ser admin o no existir).")

        conn.close()

    @staticmethod
    def modificar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena, nuevo_rol):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
        usuario = cursor.fetchone()    
        if not usuario:
            print("El usuario no existe o está inactivo.")
            conn.close()
            return False       
        if usuario["rol"] == "admin":
            print("No se puede modificar a otro administrador.")
            conn.close()
            return False       
        cursor.execute("""
        UPDATE usuarios SET nombre = %s, apellido = %s, telefono = %s, contrasena = %s, rol = %s WHERE id = %s
        """, (nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena, nuevo_rol, id_usuario))
        conn.commit()
        conn.close()
        print("Usuario modificado con éxito.")
        return True

class anfitrion(usuario):
    pass

class turista(usuario):
    pass
