"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
el número de teléfono sin el prefijo y la extensión."""

def mostrar_telefono(telefono,partes,numero):
    return numero

if __name__=="__main__":

    telefono = input("Introduce el número de teléfono en el siguiente formato (+34-XXXXXXXXX-XX): ")
    # Separar el número en sus partes (prefijo, número, extensión)
    partes = telefono.split('-')
    numero = partes[1]
    # Mostrar el número sin el prefijo y la extensión
    print (mostrar_telefono(telefono,partes,numero))
