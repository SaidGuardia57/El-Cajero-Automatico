# Cajero Automático en Python

Este proyecto simula el funcionamiento básico de un cajero automático utilizando Python.

---

## Descripción

El programa permite a los usuarios ingresar mediante un PIN y realizar diferentes operaciones bancarias como consultar saldo, depositar dinero, retirar dinero y ver el historial de movimientos.

El sistema funciona mediante un menú interactivo que se mantiene activo hasta que el usuario decide salir.

---

## Funcionalidades

- Inicio de sesión con PIN
- Soporte para múltiples usuarios
- Consulta de saldo
- Depósito de dinero
- Retiro de dinero
- Historial de movimientos
- Menú interactivo con bucle while
- Uso de estructuras if, elif, else

---

## Estructura del proyecto

login.py  
deposito.py  
retiro.py  
historial.py  
main.py  

---

## Cómo ejecutar

1. Tener Python instalado  
2. Ejecutar el archivo principal:

python main.py

---

## Usuarios de prueba

- 1234 → saldo inicial: $1000  
- 5678 → saldo inicial: $500  

---

## Funcionamiento

1. El usuario ingresa su PIN  
2. Si es correcto, accede al menú  
3. Puede elegir entre:
   - Consultar saldo  
   - Depositar dinero  
   - Retirar dinero  
   - Ver historial  
   - Salir  
4. Todas las operaciones actualizan el saldo y se registran en el historial  

---

## Consideraciones

- No se permite retirar más dinero del disponible  
- El sistema limita los intentos de PIN  
- El historial guarda todos los movimientos realizados  

---

## Trabajo en equipo

El proyecto fue desarrollado utilizando GitHub y trabajo por ramas:

- login → sistema de acceso con PIN  
- deposito → lógica de depósitos  
- retiro → lógica de retiros  
- historial → registro de movimientos  
- main → integración del sistema  

---

## Tecnologías utilizadas

- Python
- Git & GitHub

---

## Integrantes del grupo

- David Philo  
- Said Guardia  
- María Cedeño  
- Jerry Cedeño
- Gian Pitti  
- Adriana Cervera  

---

## Nota

Proyecto desarrollado como práctica de programación y uso de estructuras de control en Python, junto con el uso de GitHub para trabajo colaborativo.
