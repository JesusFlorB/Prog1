"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

def obtener_euros_y_centimos(precio):
    euros = int(precio)
    centimos = int((precio - euros) * 100)
    return euros, centimos

if __name__=="__main__":

    precio_producto = float(input("Por favor, ingrese el precio del producto en euros (con dos decimales): "))

    # Llamar a la función para obtener euros y céntimos
    euros, centimos = obtener_euros_y_centimos(precio_producto)

    print(f"El precio ingresado es de {euros} euros y {centimos} céntimos.")
