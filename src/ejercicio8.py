"""Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes"""


while 1: 
    try:
        #lista vacia para guardar los numeros que ingrese el usuario
        num = []
        #ciclo for para capturar los numeros
        for i in range(3):
            #pedir al usuario ingresar los numeros
            numeros = int(input("Por favor introduce tres numeros: ")) 
            #guardar cada numero en la lista
            num.append(numeros)
        sumaNumeros = sum(num)
        print(sumaNumeros)
        exit()
    except ValueError:
    #enviar alerta cuando el usuario introduzca un valor incorrecto
        print("ERROR. Introduzca un numero de tipo entero")