from auth import validar_precio
from conexion import conectar

class hospedaje:
    def __init__(self, id, anfitrion_id, titulo, descripcion, precio):
        self.id = id
        self.anfitrion_id = anfitrion_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio = precio

def registrar_hospedaje(usuario):
    print("\n<<< Rgistrar nuevo hospedaje >>>")
    titulo = input("Título del hospedaje: ").strip()
    descripcion = input("Descripción del hospedaje: ").strip() 
    precio = validar_precio()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ubicaciones")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO ubicaciones (ciudad, provincia) VALUES ('Sin definir en este sprint', 'Sin definir en este sprint')")
        conn.commit()

    cursor.execute("SELECT COUNT(*) FROM categorias")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO categorias (nombre) VALUES ('Sin definir en este sprint')")
        conn.commit()
    cursor.execute("SELECT id FROM categorias WHERE nombre = 'Sin definir en este sprint'")
    categoria_id = cursor.fetchone()[0]
        


    cursor.execute("""
    INSERT INTO hospedajes (anfitrion_id, titulo, descripcion, precio_por_noche, capacidad, direccion, ubicacion_id, categoria_id, disponible)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1)
""", (usuario.id, titulo, descripcion, precio, 1, "Dirección no definida para este sprint", 1, categoria_id))
    conn.commit()
    conn.close()
    print("\nHospedaje registrado con éxito.")

def mostrar_hospedaje_registrado(usuario):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, titulo, descripcion, precio_por_noche
        FROM hospedajes
        WHERE anfitrion_id = %s AND activo = 1
    """, (usuario.id,))
    hospedajes = cursor.fetchall()
    conn.close()

    print("\n<<< Tus hospedajes publicados >>>")
    if not hospedajes:
        print("No tenés ningún hospedaje registrado.")
    else:
        for i, h in enumerate(hospedajes, 1):
            print(f"{i}. {h['titulo']} {h['descripcion']} (${h['precio_por_noche']}/noche)")


def eliminar_hospedaje(usuario):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT id, titulo FROM hospedajes
    WHERE anfitrion_id = %s
""", (usuario.id,))
    hospedajes = cursor.fetchall()

    if not hospedajes:
        print("No tenés ningún hospedaje registrado.")
        conn.close()
        return
    
    print("\n<<< Eliminar hospedaje >>>")
    for i, h in enumerate(hospedajes, 1):
        print(f"{i}. {h['titulo']}")

    opcion = input("Elegí el número del hospedaje que deseas eliminar: ").strip()
    if opcion.isdigit():
        opcion = int(opcion) - 1
        if 0 <= opcion < len(hospedajes):
            id_hospedaje = hospedajes[opcion]["id"]
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hospedajes WHERE id = %s", (id_hospedaje,))
            conn.commit()
            print("Hospedaje eliminado con éxito.")
        else:
            print("Opción inválida.")
    else:
        print("Por favor ingresar un número válido.")
    conn.close()

def mostrar_hospedaje():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT titulo, descripcion, precio_por_noche, disponible
    FROM hospedajes
    WHERE disponible = 1
""")
    hospedajes = cursor.fetchall()
    conn.close()

    print("\n<<< Hospedajes publicados en RoomsyDevs >>>")
    if not hospedajes:
        print("No hay hospedajes publicados.")
    else:
        for i, h in enumerate(hospedajes, 1):
            print(f"{i}. {h['titulo']} (${h['precio_por_noche']}/noche)")
            print(f"{h['descripcion']}")

def disponibilidad_hospedaje(usuario):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT id, titulo, disponible FROM hospedajes
    WHERE anfitrion_id = %s AND activo = 1
""", (usuario.id,))
    hospedajes = cursor.fetchall()

    if not hospedajes:
        print("No tenés ningún hospedaje registrado.")
        conn.close()
        return
    
    print("\n<<< Cambiar disponibilidad de hospedaje >>>")
    for i, h in enumerate(hospedajes, 1):
        estado = "Disponible" if h["disponible"] == 1 else "No disponible"
        print(f"{i}. {h['titulo']} ({estado})")

    opcion = input("Elegí el número del hospedaje que deseas modificar: ").strip()
    if opcion.isdigit():
        opcion = int(opcion) - 1
        if 0 <= opcion < len(hospedajes):
            id_hospedaje = hospedajes[opcion]["id"]
            nuevo_estado = input ("¿Te gustaría poner el hospedaje como Disponible (1) o como No disponible (0)? ").strip()
            if nuevo_estado in ["0", "1"]:
                cursor = conn.cursor()
                cursor.execute("UPDATE hospedajes SET disponible = %s WHERE id = %s", (int(nuevo_estado), id_hospedaje))
                conn.commit()
                print("Estado de disponibilidad actualizado.")
            else:
                print("Tipo de estado inválido, por favor ingrese 1 o 0.")
        else:
            print("Opción inválida.")
    else:
        print("Debe ingresar un número válido")
    conn.close()