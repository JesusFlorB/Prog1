"""Escribe un programa que pida el importe sin IVA de un artículo 
y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

def Total(precio,IVA):
    Importe = precio * (1 + (IVA / 100))
    return f"El coste final es {Importe} euros"

if __name__=="__main__":
    
    precio = int(input("Escribe el precio del producto sin IVA: "))
    IVA = int(input("Escribe el IVA que se le aplicara al producto: "))

    print (Total(precio,IVA))