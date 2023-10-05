"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: 
"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, 
y c y r son el cociente y el resto de la división entera respectivamente."""

def division(n,m,c,r):
    c = n // m  # cociente
    r = n % m   # resto
    return f"La división de {n} entre {m} da un cociente {c} y un resto {r}."

if __name__=="__main__":

    n = int(input("Introduce el primer número entero (n): "))
    m = int(input("Introduce el segundo número entero (m): "))

    # Calcular el cociente y el resto de la división
    c = n // m  # cociente
    r = n % m   # resto

    print(division(n,m,c,r))