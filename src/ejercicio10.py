"""Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética"""

def resultadoOperacion(operando1,operando2,operando3):
    operacion = (operando1 + operando2 / operando2 * operando3) ** operando2
    return f"El resultado de la operacion es {operacion}"

if __name__=="__main__":

    #entrada
    operando1 = 3
    operando2 = 2
    operando3 = 5

    #salida
    print (resultadoOperacion(operando1,operando2,operando3))