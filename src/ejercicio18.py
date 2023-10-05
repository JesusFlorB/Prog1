"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""


def obtener_nombre_completo():
    nombre_completo = input("Introduce tu nombre completo: ")
    return nombre_completo

if __name__=="__main__":

    def mostrar_formas_nombre(nombre_completo):
        print(f"Nombre completo en minúsculas: {nombre_completo.lower()}")
        print(f"Nombre completo en mayúsculas: {nombre_completo.upper()}")

        partes = nombre_completo.split()
        nombre = partes[0]
        primer_apellido = partes[1]
        segundo_apellido = partes[2]

        nombre_apellidos_mayuscula = f"{nombre.capitalize()} {primer_apellido.capitalize()} {segundo_apellido.capitalize()}"
        print(f"Nombre con primera letra y apellidos con primera letra en mayúscula: {nombre_apellidos_mayuscula}")

    #obtener el nombre completo del usuario
    nombre_completo = obtener_nombre_completo()

    #mostrar el nombre completo en diferentes formas
    mostrar_formas_nombre(nombre_completo)