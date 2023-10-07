"""¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo."""

def solicitar_numero():
    return float(input("Por favor, ingresa un número: "))

def calcular_suma():
    return solicitar_numero() + solicitar_numero() + solicitar_numero()

def imprimir_suma():
    print(f"La suma de los tres números es: {calcular_suma()}")
    
if __name__ == "__main__":
    
    imprimir_suma()

