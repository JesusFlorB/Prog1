"""Escribir un programa que pregunte el nombre del usuario en la consola 
y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", 
donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre."""

def nombre_tiene_letras(num_letras,nombre_mayusculas,nombre):
    return f"{nombre} tiene {num_letras} letras"

if __name__=="__main__":
    
    nombre = input("Introduce tu nombre: ")
    
    # Obtener la longitud del nombre
    num_letras = len(nombre)

    # Convertir el nombre a mayúsculas
    nombre_mayusculas = nombre.upper()
    
    print(f"{nombre_mayusculas} tiene {num_letras} letras")
