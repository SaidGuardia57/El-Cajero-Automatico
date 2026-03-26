def ver_historial(historial):
    print("\n--- HISTORIAL ---")

    if not historial:
        print("No hay movimientos\n")
    else:
        for movimiento in historial:
            print(movimiento)
        print()
