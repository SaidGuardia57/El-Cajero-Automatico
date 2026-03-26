def depositar(saldo, historial):
    try:
        monto = float(input("Ingresa el monto a depositar: "))
    except:
        print("Monto inválido\n")
        return saldo

    if monto > 0:
        saldo += monto
        historial.append(f"Depósito: +${monto}")
        print(f"Depósito exitoso. Nuevo saldo: ${saldo}\n")
    else:
        print("El monto debe ser mayor a 0\n")

    return saldo