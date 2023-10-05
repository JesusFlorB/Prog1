"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

def frase_letra_modificada(frase,vocal,frase_modificada):
    return frase_modificada

if __name__=="__main__":
    
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")
    #verificar si la entrada es una vocal
    if vocal.lower() in 'aeiou':
        # Reemplazar la vocal en la frase por su versión en mayúscula
        frase_modificada = frase.replace(vocal,vocal.upper())
        
        #mostrar la frase modificada
        print(frase_modificada)
    else:
        print ("La entrada no es corrrecta")