"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""


def suma(numeroUNO,numeroDOS,numeroTRES):
    numerosSumados = numeroUNO + numeroDOS + numeroTRES
    return f"La suma de los tres numeros es {numerosSumados}"

if __name__=="__main__":
    
    #entrada
    numeroUNO = int(input("Escribe el primer numero: "))
    numeroDOS = int(input("Escribe el segundo numero: "))
    numeroTRES = int(input("Escribe el tercer numero: "))
    
    #salida
    print (suma(numeroUNO,numeroDOS,numeroTRES))