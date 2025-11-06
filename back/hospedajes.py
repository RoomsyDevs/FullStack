from validaciones import Auth as auth
from conexion import conectar

auth = auth()
class hospedaje:
    def __init__(self, id, anfitrion_id, titulo, descripcion, precio_por_noche, ciudad, provincia, capacidad):
        self.id = id
        self.anfitrion_id = anfitrion_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio_por_noche = auth.validar_precio
        self.ciudad = ciudad
        self.provincia = provincia
        self.capacidad = capacidad

    @classmethod
    def registrar_hospedaje(cls, anfitrion_id, titulo, precio_por_noche, descripcion, ciudad, provincia, capacidad):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id FROM ubicaciones WHERE ciudad = %s AND provincia = %s
        """, (ciudad, provincia))
        resultado = cursor.fetchone()
        if resultado:
            ubicacion_id = resultado[0]
        else:

        # Insertar ubicación
            cursor.execute("""INSERT INTO ubicaciones (ciudad, provincia) VALUES (%s, %s)
            """, (ciudad, provincia))
            ubicacion_id = cursor.lastrowid

        # Insertar categoría automaticamente (no contemplada para este sprint)
        cursor.execute("SELECT COUNT(*) FROM categorias")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO categorias (nombre) VALUES ('Sin definir en este sprint')")
            conn.commit()
        cursor.execute("SELECT id FROM categorias WHERE nombre = 'Sin definir en este sprint'")
        categoria_id = cursor.fetchone()[0]

        # Insertar hospedaje
        cursor.execute("""
        INSERT INTO hospedajes (anfitrion_id, titulo, precio_por_noche, descripcion, ubicacion_id, categoria_id, capacidad)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (anfitrion_id, titulo, precio_por_noche, descripcion, ubicacion_id, categoria_id, capacidad))

        conn.commit()
        conn.close()
        print("\nHospedaje registrado correctamente.")

    @classmethod
    def mostrar_hospedaje_registrado(cls, usuario):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, titulo, descripcion, precio_por_noche
            FROM hospedajes
            WHERE anfitrion_id = %s AND disponible = 1
        """, (usuario.id,))
        hospedajes = cursor.fetchall()
        conn.close()

        print("\n<<< Tus hospedajes publicados >>>")
        if not hospedajes:
            print("No tenés ningún hospedaje registrado.")
        else:
            for i, h in enumerate(hospedajes, 1):
                print(f"{i}. {h['titulo']} {h['descripcion']} (${h['precio_por_noche']}/noche)")
        conn.close()

    @classmethod
    def eliminar_hospedaje(cls, usuario):
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

    @classmethod
    def mostrar_hospedaje(cls):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT h.titulo, h.descripcion, h.precio_por_noche, h.disponible,
        u.ciudad, u.provincia
        FROM hospedajes h
        JOIN ubicaciones u ON h.ubicacion_id = u.id
        WHERE h.disponible = 1
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
                print(f"{h['ciudad']}, {h['provincia']}\n")

    @classmethod
    def disponibilidad_hospedaje(cls, usuario):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT id, titulo, disponible FROM hospedajes
        WHERE anfitrion_id = %s
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