"""Suponiendo que se han ejecutado las siguientes sentencias de asignación:

ancho = 17
alto = 12.0

Para cada una de las expresiones siguientes, calcula el valor de las expresiones:

1. ancho / 2
2. ancho // 2
3. alto / 3
4. 1 + 2 * 5"""

def valores(ancho,alto):
    operacion1 = ancho / 2
    operacion2 = ancho // 2
    operacion3 = alto / 3
    operacion4 = 1 + 2 * 5
    return f"El resultado 1 es {operacion1}\nEl resultado 2 es {operacion2}\nEl resultado 3 es {operacion3}\nEl resultado 4 es {operacion4}"

if __name__=="__main__":

#valores
    ancho = 17
    alto = 12.0

    print (valores(ancho,alto))