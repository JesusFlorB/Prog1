"""Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes"""


def obtener_tres_numeros():
    num = []  #lista vacía para guardar los números ingresados por el usuario
    for i in range(3):
        while True:
            try:
                numeros = int(input("Por favor introduce tres numeros: "))
                num.append(numeros)
                break  #salir del bucle si el usuario ingresó un número válido
            except ValueError:
                print("ERROR. Introduzca un número de tipo entero")
    return num

def calcular_suma(lista_numeros):
    suma_numeros = sum(lista_numeros)
    return suma_numeros

if __name__ == "__main__":
    numeros = obtener_tres_numeros()
    suma_numeros = calcular_suma(numeros)
    print(suma_numeros)
