"""Escribe un programa que pida el nombre del usuario para luego darle la bienvenida."""

def saludo(nombre):
    return "hola "+ nombre

if __name__=="__main__":
    
    nombre = input("Por favor, dime tu nombre: ")

    print(saludo(nombre))