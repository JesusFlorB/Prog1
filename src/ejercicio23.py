"""Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es."""

def cambiar_dominio_correo(correo_original):
    partes = correo_original.split('@')
    nombre = partes[0]
    nuevo_correo = nombre + '@ceu.es'
    return nuevo_correo

if __name__=="__main__":

    correo_original = input("Por favor, ingrese su correo electrónico: ")

    #llamar a la función para cambiar el dominio
    nuevo_correo = cambiar_dominio_correo(correo_original)

    #mostrar el nuevo correo electrónico
    print (nuevo_correo)
