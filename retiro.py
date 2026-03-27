#retiro.py

def retirar(saldo, historial):
    try:
        monto = float(input("Ingresa el monto a retirar: "))
    except:
        print("Monto inválido\n")
        return saldo

    if monto > saldo:
        print("Fondos insuficientes\n")
    elif monto <= 0:
        print("Monto inválido\n")
    else:
        saldo -= monto
        historial.append(f"Retiro: -${monto}")
        print(f"Retiro exitoso. Nuevo saldo: ${saldo}\n")

    return saldo
