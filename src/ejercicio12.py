"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase: "tu índice de masa corporal es"
donde el índice de masa corporal calculado sea redondeado con dos decimales."""

def calculoIMC(peso,estatura):
    imc = peso / pow(estatura, 2)
    imc = round(imc, 2)
    return f"Tu indice de masa corporal es {imc}"
    
if __name__=="__main__":

    peso = float(input("Ingresa tu peso en kg: "))
    estatura = float(input("Ingresa tu estatura en metros: "))

    #calcular el índice de masa corporal (IMC)
    imc = peso / (estatura**2)

    #redondear el IMC a dos decimales
    imc = round(imc, 2)

    print (calculoIMC(peso,estatura))
