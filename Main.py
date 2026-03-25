#main.py

from login import iniciar_sesion
from deposito import depositar
from retiro import retirar
from historial import ver_historial


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
            continue
