"""Escribir un programa que pida al usuario que introduzca una frase en la consola 
y muestre por pantalla la frase invertida."""

def invertir_frase(frase,frase_invertida):
    return frase_invertida
    
    
if __name__=="__main__":
    
    frase = input("Introduce una frase: ")
    #Invertir la frase
    frase_invertida = frase[::-1]
    # Mostrar la frase invertida
    print (invertir_frase(frase,frase_invertida))
