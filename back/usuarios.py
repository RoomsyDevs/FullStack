from conexion import conectar

class usuario:
    def __init__(self, id, nombre, apellido, email, contrasena, rol, telefono):
        self.id= id
        self.nombre = nombre
        self.apellido = apellido
        self.email= email
        self.contrasena = contrasena
        self.rol = rol
        self.telefono = telefono    

class admin(usuario):
    def __init__(self, id, nombre, apellido, email, contrasena, username):
        super().__init__(id, nombre, apellido, email, contrasena, "admin", telefono="N/A")
        self.username = username

class anfitrion(usuario):
    pass

class turista(usuario):
    pass

def registrar_usuario(nombre, apellido, email, contrasena, telefono, rol, username=None):
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

def iniciar_sesion(email, contrasena):
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
    
def modificar_cuenta(usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE usuarios
        SET nombre = %s, apellido = %s, telefono = %s, contrasena = %s
        WHERE id = %s
    """, (nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena, usuario.id))
    conn.commit()
    conn.close()

def eliminar_cuenta(usuario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET estado = 0 WHERE id = %s", (usuario.id,))
    conn.commit()
    conn.close()

def mostrar_usuarios():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE estado = 1")
    usuarios = cursor.fetchall()
    conn.close()

    for u in usuarios:
        print(f"{u['id']}. {u['nombre']} {u['apellido']} {u['email']} ({u['rol']})")

def modificar_usuario(id_usuario, nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
    usuario = cursor.fetchone()

    if usuario and usuario ["rol"] != "admin":
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE usuarios SET nombre = %s, apellido = %s, telefono = %s, contrasena = %s WHERE id = %s
        """, (nuevo_nombre, nuevo_apellido, nuevo_telefono, nueva_contrasena, id_usuario))
        conn.commit()
        conn.close()

def eliminar_usuario(id_usuario):
    conn = conectar()
    cursor = conn. cursor (dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s AND estado = 1", (id_usuario,))
    usuario = cursor.fetchone()

    if usuario and usuario["rol"] != "admin":
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET estado = 0 WHERE id = %s", (id_usuario,))
        conn.commit()
        conn.close

def crear_admin(nombre, apellido, email, contrasena, username):
    registrar_usuario(nombre, apellido, email, contrasena, telefono="N/A", rol="admin", username=username)
    return True
