#login.py

def iniciar_sesion(usuarios):
    intentos = 3

    while intentos > 0:
        pin = input("Ingresa tu PIN: ")

        if pin in usuarios:
            print("Acceso concedido\n")
            return pin  # usuario activo
        else:
            intentos -= 1
            print(f"PIN incorrecto. Intentos restantes: {intentos}\n")

    print("Acceso bloqueado")
    return None
