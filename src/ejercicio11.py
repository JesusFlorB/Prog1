"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después"""
"""muestre en pantalla la suma de todos los enteros desde 1 hasta n."""
"""La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: (n*(n+1))//2"""

def sumaEnteros(n):
    suma = (n * (n + 1)) // 2
    return f"La suma de los enteros desde 1 hasta n es {suma}"

if __name__=="__main__":
    
    n = int(input("Ingrese un entero positivo: "))

    #verificamos si el número ingresado es positivo
    if n <= 0:
        print("Por favor, ingrese un entero positivo.")
    else:
        suma = (n * (n + 1)) // 2
        
        print (sumaEnteros(n))