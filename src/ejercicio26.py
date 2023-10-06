"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos en una línea distinta."""

def mostrar_productos():
    productos = input("Por favor, ingresa los productos separados por comas: ")
    lista_productos = productos.split(',')
    for producto in lista_productos:
        print(producto.strip())

#llamar a la función para mostrar los productos
mostrar_productos()