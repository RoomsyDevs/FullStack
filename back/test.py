from conexion import conectar

try:
    conn = conectar()
    print("✅ Conexión exitosa a RoomsyDevs.")
    conn.close()
except Exception as e:
    print("❌ Error al conectar:", e)
