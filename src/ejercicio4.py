"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, 
la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida."""

def temperatura(Fahrenheit):
    return f"La temperatura es {Fahrenheit} grados Fahrenheit"

if __name__=="__main__":
    
    Celsius = int(input("Por favor, escribe la temperatura en grados Celsius que quieres convertir en Fahrenheit: "))

    #pasar celsius a fahrenheit
    Fahrenheit = Celsius * 9/5 + 32

    print(temperatura(Fahrenheit))