# auth.py --> módulo de autenticación

def validar_email():
    dominios_validos = ["@gmail.com", "@outlook.com", "@hotmail.com"]
    while True:
        email = input("Email: ").strip()
        if any(email.endswith(dominio) for dominio in dominios_validos):
            return email
        print("\nError: el email debe finalizar con un dominio válido.")

def validar_email_unico(usuarios, email_actual=None):
    while True:
        email = validar_email()

        # Permitimos dejar el mismo email si no se quiere cambiar
        if email == email_actual:
            return email

        if any(u.email == email for u in usuarios):
            print("\nError: Este email ya está registrado. Intente nuevamente.")
        else:
            return email

def validar_telefono(numero):
    numeros_validos = "0123456789"
    if len(numero) < 10 or len(numero) > 11:
        return False

    for caracter in numero:
        if caracter not in numeros_validos:
            return False
    return True

def validar_rol():
    while True:
        rol = input("Rol (admin / turista / anfitrion): ").strip().lower()
        if rol in ["admin", "turista", "anfitrion"]:
            return rol
        print("\nError: el rol solo puede ser 'admin' o 'estandar' ")

def validar_contrasena():
    while True:
        contrasena = input("Contraseña (mínimo 6 caracteres): ").strip()
        if len(contrasena) >= 6:
            return contrasena
        print("\nError: La contraseña debe tener al menos 6 caracteres.")

def validar_login(usuario, contrasena):
    intentos = 3
    while intentos > 0:
        if contrasena == usuario.contrasena:
            return True
        intentos -= 1
        contrasena = input("Contraseña incorrecta, por favor intente de nuevo: ")
        print("Demasiados intentos fallidos.")
        return False