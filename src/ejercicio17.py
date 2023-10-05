"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""


def imprimir_nombre_multiples_veces(nombre, numero):
    for _ in range(numero):
        print(nombre)
        
if __name__=="__main__":

    nombre = input("Introduce tu nombre: ")
    numero = int(input("Introduce un número entero: "))
    imprimir_nombre_multiples_veces(nombre, numero)
