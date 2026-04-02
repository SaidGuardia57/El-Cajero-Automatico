#main.py

import os
from login import iniciar_sesion
from deposito import depositar
from retiro import retirar
from historial import ver_historial


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("💰 Bienvenido a tu Cajero Automático\n")

    # Usuarios con PIN y saldo
    usuarios = {
        "1234": {"saldo": 1000, "historial": []},
        "4570": {"saldo": 5000, "historial": []},
        "8253": {"saldo": 50, "historial": []},
        "3005": {"saldo": 0, "historial": []},
        "5678": {"saldo": 2500, "historial": []}
    }

    usuario_actual = iniciar_sesion(usuarios)

    if not usuario_actual:
        return

    saldo = usuarios[usuario_actual]["saldo"]
    historial = usuarios[usuario_actual]["historial"]

    opcion = 0

    while opcion != 5:
        limpiar_pantalla()
        print("\n--- MENÚ ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial")
        print("5. Salir")

        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            print("Opción inválida")
            input("\nPresiona Enter para volver al menú...")
            continue

        limpiar_pantalla()

        if opcion == 1:
            print("--- CONSULTAR SALDO ---\n")
            print(f"Tu saldo es: ${saldo}\n")
            input("Presiona Enter para volver al menú...")

        elif opcion == 2:
            print("--- DEPOSITAR DINERO ---\n")
            saldo = depositar(saldo, historial)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == 3:
            print("--- RETIRAR DINERO ---\n")
            saldo = retirar(saldo, historial)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == 4:
            print("--- HISTORIAL ---\n")
            ver_historial(historial)
            input("\nPresiona Enter para volver al menú...")

        elif opcion == 5:
            limpiar_pantalla()
            print("Gracias por usar el cajero 👋")

        else:
            print("Opción inválida")
            input("\nPresiona Enter para volver al menú...")

    # Guardar cambios
    usuarios[usuario_actual]["saldo"] = saldo


if __name__ == "__main__":
    main()