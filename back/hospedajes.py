hospedajes = []
def registrar_hospedaje(anfitrion):
    print("n\<<< Registrar nuevo hospedaje >>>")
    titulo = input("Título del hospedaje: ").strip()
    descripcion = input("Descripción del hospedaje: ").strip()
    precio = input("Precio por noche: ").strip()

    hospedaje = {
        "anfitrion": anfitrion.email,
        "titulo": titulo,
        "descripcion": descripcion,
        "precio": precio
    }
    
    hospedajes.append(hospedaje)
    print("\nHospedaje registrado!!")

def mostrar_hospedaje_registrado(anfitrion):
    print("\n<<< Tus hospedajes publicados >>>")
    encontrados = [h for h in hospedajes if h["anfitrion"] == anfitrion.email]
    if not encontrados:
        print("No tenés hospedajes registrados.")
    else:
        for i, h in enumerate(encontrados, 1):
            print(f"{i}. {h['titulo']} - {h['descripcion']} (${h['precio']}/noche)")

def eliminar_hospedaje(anfitrion):
    mostrar_hospedaje_registrado(anfitrion)
    encontrados = [h for h in hospedajes if h["anfitrion"] == anfitrion.email]
    if not encontrados:
        return
    
    opciones = int(input("Elija el número del hospedaje que desea eliminar: ")) - 1
    if 0 <= opciones < len(encontrados):
        hospedajes.remove(encontrados[opciones])
        print("Hospedaje eliminado con éxito.")
    else:
        print("Opción no válida.")


def mostrar_hospedajes():
    print("\n<<< Hospedajes disponibles >>>")
    if not hospedajes:
        print("No hay hospedajes publicados")
    else:
        for i, h in enumerate(hospedajes, 1):
            print(f"{i}. {h['titulo']} - (${h['precio']}/noche)")
            print(f"{h['descripcion']}")